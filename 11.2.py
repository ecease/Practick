# Кондратюк Егор 3ИСд-1.22
# Практическая №11 Вариант 17
#Двухмерный массив размером п х т содержит некоторые буквы русского алфавита, расположенные в произвольном порядке. Определить, можно ли из этих букв составить заданное слово S. (Каждую букву массива использовать не более одного раза.)



def can_form_word(matrix, word):
    from collections import Counter
    
    # Собир все букв из двумер массива в один список
    all_letters = [letter for row in matrix for letter in row]
    
    # Счит сколько раз встречат каждая буква
    letters_count = Counter(all_letters)
    word_count = Counter(word)
    
    # Проверям достаточ ли букв в матрице, чтобы состав слово
    for char, needed in word_count.items():
        if letters_count[char] < needed:
            return False
    return True

# Пример букв
m = [
    ['к','р','о','в'],
    ['р','к','а','с'],
    ['т','у','к','а']
]
s = "абоба" # краска, картук он сможет составить

if can_form_word(m, s):
    print("Можно составить слово:", s)
else:
    print("Нельзя составить слово:", s)
