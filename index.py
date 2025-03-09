from datetime import datetime, timedelta
import random
import re

#Завдання 1
def get_days_from_today(date: str):
    try:
        today = datetime.now()
        date = datetime.strptime(date, '%Y-%m-%d')
        return (today - date).days
    except ValueError:
        return 'Invalid date format'

amount_of_days_1 = get_days_from_today('2025.03.07')
amount_of_days_2 = get_days_from_today('2025-08-09')
amount_of_days_3 = get_days_from_today('2023-05-09')
print(amount_of_days_1)
print(amount_of_days_2)
print(amount_of_days_3)


#Завдання 2
def get_numbers_ticket(min, max, quantity) -> list:
    # створюємо set для зберігання унікальних чисел
    random_numbers_set = set()

    # переконуємося, що вхідні дані коректні
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        if min < 1 or max > 1000 or quantity < 1:
            return []

        while len(random_numbers_set) < quantity:
            random_numbers_set.add(random.randint(min, max))

        numbers_list = list(random_numbers_set)
        numbers_list.sort()

        return numbers_list
    except ValueError:
        print('Incorrect input')
        return []


numbers_ticket_1 = get_numbers_ticket(1, 1000, 6)
print(numbers_ticket_1)

# Завдання 3
"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
def normalize_phone(phone_number):
    if not phone_number:  # Перевірка на порожнє значення
        return ""

    phone_number = re.sub(r"[^0-9+]", "", phone_number.strip())  # Очищення від зайвих символів

    if phone_number.startswith('38'):
        phone_number = '+' + phone_number
    elif phone_number.startswith('0'):
        phone_number = '+38' + phone_number

    return phone_number

print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("38050-111-22-22   "))

# Завдання 4
def get_upcoming_birthdays(users: list):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Переносимо день народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження в наступні 7 днів
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            # Переносимо привітання, якщо випадає на вихідний
            if birthday_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
        # Додатково перевіряємо вихідні перед поточним понеділком
        if today.weekday() == 0 and birthday_this_year.weekday() in [5, 6]:
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": today.strftime("%Y.%m.%d")  # Сьогоднішній понеділок
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "John Doe 2", "birthday": "1985.03.08"},
    {"name": "John Doe 3", "birthday": "1985.03.14"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
