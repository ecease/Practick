#Кондратюк Егор 3ИСд-1.22
#Практическая 13 вариант 8
# Записать в файл последовательного доступа N натуральных
#чисел: а 1г а2, ..., аЛ, полученных с помощью датчика случайных чисел. Сформировать новый файл последовательного доступа с числами 




import random

def main():
    N = int(input("Введите количество чисел: "))

    # Генерация и запись в первый файл
    numbers = [random.randint(1, 100) for _ in range(N)]
    with open("file1.txt", "w", encoding="utf-8") as f1:
        for num in numbers:
            f1.write(str(num) + "\n")

    # Формирование нового списка
    new_numbers = []
    for i in range(0, N, 2):
        
        if i + 1 < N:
            new_numbers.append(numbers[i])         
            new_numbers.append(numbers[i + 1])     
            new_numbers.append(numbers[i] * numbers[i + 1])  
        else:
            
            new_numbers.append(numbers[i])

    # Запись результата во втором файле
    with open("file2.txt", "w", encoding="utf-8") as f2:
        for num in new_numbers:
            f2.write(str(num) + "\n")


main()
