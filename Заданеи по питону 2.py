import csv
import json
from datetime import datetime

# Данные сотрудников
employees = [
    {"ФИО": "Иванов Иван Иванович", "Должность": "Менеджер", "Дата найма": "22.10.2013", "Оклад": 250000},
    {"ФИО": "Сорокина Екатерина Матвеевна", "Должность": "Аналитик", "Дата найма": "12.03.2020", "Оклад": 75000},
    {"ФИО": "Струков Иван Сергеевич", "Должность": "Старший программист", "Дата найма": "23.04.2012", "Оклад": 150000},
    {"ФИО": "Корнеева Анна Игоревна", "Должность": "Ведущий программист", "Дата найма": "22.02.2015", "Оклад": 120000},
    {"ФИО": "Старчик Сергей Анатольевич", "Должность": "Младший программист", "Дата найма": "12.11.2021", "Оклад": 50000},
    {"ФИО": "Бутенко Артем Андреевич", "Должность": "Архитектор", "Дата найма": "12.02.2010", "Оклад": 200000},
    {"ФИО": "Савченко Алина Сергеевна", "Должность": "Старший аналитик", "Дата найма": "13.04.2016", "Оклад": 100000},
]

# Функция для создания CSV
def create_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Функция для создания JSON
def create_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Создание файлов
create_csv('employees.csv', employees)
create_json('employees.json', employees)
def calculate_programmer_day_bonus(employees):
    bonus_date = "13.09"
    for employee in employees:
        if "программист" in employee["Должность"].lower():
            bonus = employee["Оклад"] * 0.03
            print(f'{employee["ФИО"]} получит премию {bonus} рублей ко Дню программиста.')


def calculate_holiday_bonus(employees):
    march_8_bonus = 2000
    february_23_bonus = 2000

    # Премия к 8 марта
    for employee in employees:
        print(f'{employee["ФИО"]} получит премию {march_8_bonus} рублей к 8 марта.')

    # Премия к 23 февраля
    for employee in employees:
        # Например, выплата только мужчинам:
        if employee["ФИО"].split()[1].endswith("ич"):
            print(f'{employee["ФИО"]} получит премию {february_23_bonus} рублей к 23 февраля.')


def index_salaries(employees):
    current_year = datetime.now().year
    for employee in employees:
        hire_year = datetime.strptime(employee["Дата найма"], "%d.%m.%Y").year
        experience = current_year - hire_year

        if experience > 10:
            employee["Оклад"] += employee["Оклад"] * 0.07
        else:
            employee["Оклад"] += employee["Оклад"] * 0.05
        print(f'Индексированная зарплата {employee["ФИО"]}: {employee["Оклад"]} рублей.')


def vacation_schedule(employees):
    eligible_for_vacation = []
    current_date = datetime.now()

    for employee in employees:
        hire_date = datetime.strptime(employee["Дата найма"], "%d.%m.%Y")
        if (current_date - hire_date).days > 6 * 30:  # Больше 6 месяцев
            eligible_for_vacation.append(employee["ФИО"])

    print("Сотрудники, имеющие право на отпуск:")
    for employee in eligible_for_vacation:
        print(employee)


# Пример использования:
vacation_schedule(employees)
create_csv('updated_employees.csv', employees)
create_json('updated_employees.json', employees)
# Расчет премий
calculate_programmer_day_bonus(employees)
calculate_holiday_bonus(employees)

# Индексация зарплат
index_salaries(employees)

# Сохранение обновленных данных
create_csv('updated_employees.csv', employees)
create_json('updated_employees.json', employees)
