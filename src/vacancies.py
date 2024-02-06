class Vacancy:
    """Класс вакансии"""

    def __init__(self, name_company: str, name: str, url: str, salary_from: int, salary_to: int) -> None:
        """
        Конструктор объекта Vacancy

        :param name_company: Название компании
        :param name: Название вакансии
        :param url: Ссылка на вакансию
        :param salary_from: Нижняя граница зарплаты
        :param salary_to: Верхняя граница зарплаты
        """
        self.name_company = name_company
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Vacancy

        :return:
        """
        return f"""Название компании: {self.name_company}
                   Название вакансии: {self.name}
                   Ссылка: {self.url}
                   Зарплата: от {self.salary_from} до {self.salary_to}"""

    def __le__(self, other) -> bool:
        """
        Сравнивает текущую вакансию с другой по средней зарплате. Если значение зарплаты в какой-либо вакансии
        не указано, оно считается равным нулю

        :param other: Другая вакансия для сравнения
        :return: True, если текущая вакансия имеет меньшую или равную среднюю зарплату, иначе False
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0
            self.salary_to = 0
            if not other.salary_to and not other.salary_from:
                other.salary_from = 0
                other.salary_to = 0
                return False
            return True
        return (self.salary_from + self.salary_to / 2) <= (other.salary_from + other.salary_to / 2)
