# Кондратюк Егор 3ИСд-1.22
# Практическая №11 Вариант 17
#Дана строка. Найти в этой строке слова, которые начинаются и оканчиваются на одну и ту же букву.




slova = input("Введите строку: ")  # арка дед абоба мама папа
w = slova.split()  # Разделение на слова

filt_w = [w for w in w if w[0].lower() == w[-1].lower()]  # Фильтрация

print("Слова, которые начинаются и заканчиваются на одну букву:", filt_w)

