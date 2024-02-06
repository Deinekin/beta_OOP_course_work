from abc import ABC, abstractmethod

import requests

# from pprint import pprint



class AbstractApiHh(ABC):
    """Базовый абстрактный класс"""

    @abstractmethod
    def get_vacancies(self, vacancy: str, page: int):
        """Базовый абстрактный класс"""
        pass


class GetHhAPI(AbstractApiHh):
    """Класс для работы с api"""

    def __init__(self) -> None:
        """Сохраняем url"""
        self.__base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, vacancy: str, page: int) -> list:
        """
        Получает информацию о вакансиях с сайта hh.ru по ключевому слову

        :param vacancy: Вакансия для поиска
        :param page: Номер страницы
        :return: Список словарей
        """
        vacancies_found = []
        params = {"text": f"name:{vacancy}", "area": 2, "page": page, "per_page": 100}
        response = requests.get(url=self.__base_url, params=params)
        if response.status_code == 200:
            vacancies = response.json()
            vacancies_found.extend(vacancies["items"])
            if page == 0 and not vacancies_found:
                print("К сожалению, по Вашему запросу ничего не найдено =(")

        result: list = []
        for vacancy in vacancies_found:
            if vacancy["salary"]:
                salary = vacancy["salary"]
                if salary["from"]:
                    salary_from = salary["from"]
                else:
                    salary_from = 0
                if salary["to"]:
                    salary_to = salary["to"]
                else:
                    salary_to = 0
            else:
                salary_from = 0
                salary_to = 0
            result.append(
                {
                    "name_company": vacancy["employer"]["name"],
                    "name": vacancy["name"],
                    "url": vacancy["alternate_url"],
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                }
            )
        return result

    def get_top_n_salaries(self, vacancy: str, page: int, number_of_vacancies: int) -> list:
        """Метод для получения n самых больших зарплат"""
        list_ = self.get_vacancies(vacancy, page)
        return sorted(list_, key=lambda x: x["salary_from"], reverse=True)[:number_of_vacancies]


# hh_api = GetHhAPI()
# pprint(hh_api.get_vacancies("инженер", 0))
# pprint(hh_api.get_top_n_salaries("python324234", 0, 15))
