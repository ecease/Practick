# Кондратюк Егор 3ИСд-1.22
# Практическая №5 Вариант 18
#По номеру дня в году вывести число и месяц в общепринятой форме. Например:
#33-й день года — это 2 февраля.







day_of_year = int(input("Введите номер дня в году: "))

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
]

month_index = 0
while day_of_year > days_in_months[month_index]:
    day_of_year -= days_in_months[month_index]
    month_index += 1

print(day_of_year, month_names[month_index])
