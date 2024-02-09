from pprint import pprint

from src.add_to_json import SaveAndReadJSON
from src.API_for_vacancies import GetHhAPI


def user_interaction() -> None:
    """Главная функция для общения с пользователем"""

    name_of_vacancy = input(
        """Приветствую! Введите ключевое слово из названия вакансии для поиска предложений
    по г. Санкт-Петербург.
    Также необходимо ввести номер страницы, по которой будет осуществляться поиск.
    Данные необходимо вводить через пробел.
    За один раз можно просмотреть не более 100 вакансий\n"""
    )

    number_of_page = int(name_of_vacancy.split(" ")[-1])

    api_hh = GetHhAPI()
    hh_vacancies = api_hh.get_vacancies(name_of_vacancy[0:-2], number_of_page)
    pprint(hh_vacancies)

    user_top_salaries = int(input("Введите N для вывода топ N вакансий по зарплате\n"))
    top_salaries_vacancies = api_hh.get_top_n_salaries(name_of_vacancy[0:-2], number_of_page, user_top_salaries)
    pprint(top_salaries_vacancies)

    user_answer_save_to_json = int(
        input(
            """Желаете сохранить данные в файл?
    1 - Да, хочу сохранить все найденные вакансии
    2 - Да, хочу сохранить топ найденных по зарплате вакансий
    3 - Нет, хочу завершить работу"""
        )
    )

    json_ = SaveAndReadJSON()

    if user_answer_save_to_json == 1:
        json_.save_vacancies_to_json(hh_vacancies)
    elif user_answer_save_to_json == 2:
        json_.save_vacancies_to_json(top_salaries_vacancies)
    elif user_answer_save_to_json == 3:
        exit()

    for element in json_.read_vacancies_from_json():
        print(element)
    # pprint(json_.read_vacancies_from_json())


if __name__ == "__main__":
    user_interaction()
