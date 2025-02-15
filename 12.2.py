# Кондратюк Егор 3ИСд-1.22
# Практическая №12 Вариант 15
#Дан текст на русском языке. Напечатать в алфавитном порядке все гласные буквы, которые не входят более чем в одно слово этого текста.




# Ввод текста
text = input("Введите текст: ")

#гласные
vowels = "аеёиоуыэюя"


vowel_count = {vowel: 0 for vowel in vowels}


words = text.lower().split()
for word in words:
    unique_vowels_in_word = set(word) & set(vowels)  # Найти гласные в слове
    for vowel in unique_vowels_in_word:
        vowel_count[vowel] += 1  # Увеличиваем счётчик для этой гласной

# Выбираем только которые попадаются в одном слове
rare_vowels = sorted([v for v, count in vowel_count.items() if count == 1])


print("Гласные, которые встречаются не более чем в одном слове:", " ".join(rare_vowels))
