import json
import os

from src.vacancies import Vacancy


class SaveAndReadJSON:
    """Класс для работы с json"""

    def __init__(self, filename="vacancy.json"):
        self.__filename = filename

    def save_vacancies_to_json(self, vacancies: list) -> None:
        """Запись в JSON"""
        if os.stat(self.__filename).st_size == 0:
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
        else:
            with open(self.__filename, "r+", encoding="utf-8") as f:
                vacancies_ = json.load(f)
                for e in vacancies:
                    vacancies_.append(e)
            open("filename", "w").close()
            with open(self.__filename, "r+", encoding="utf-8") as f:
                json.dump(vacancies_, f, ensure_ascii=False, indent=4)

    def read_vacancies_from_json(self) -> list:
        """Чтение из файла, возвращает список вакансий"""
        with open(self.__filename, encoding="utf-8") as f:
            vacancies = json.load(f)
        list_of_vacancies: list = []
        for vacancy in vacancies:
            list_of_vacancies.append(Vacancy(*vacancy.values()))
        return list_of_vacancies


# hhh = SaveAndReadJSON()
# # print(hhh.read_vacancies_from_json())
# hhh.save_vacancies_to_json(
#     [
#         {
#             "name_company": "Алабуга, ОЭЗ ППТ",
#             "name": "Middle Backend-разработчик (Python)",
#             "url": "https://hh.ru/vacancy/90337366",
#             "salary_from": 200000,
#             "salary_to": 0
#         }
#     ])

# for element in hhh.read_vacancies_from_json():
#   print(element)
