# Кондратюк Егор 3ИСд-1.22
# Практическая №10 Вариант 16
#Дана квадратная матрица A[N,N].Записать на место отрицательных элементов этой матрицы нули, а на место положительных элементов — единицы. Вывести на печать нижнюю треугольную матрицу в общепринятом виде.



N = int(input("Введите размер матрицы N: "))
A = []
print("Введите матрицу построчно:")
for i in range(N):
    row = list(map(int, input().split()))
    # Сразу заменяем элементы
    for j in range(N):
        if row[j] < 0:
            row[j] = 0
        else:
            row[j] = 1
    A.append(row)

print("Нижняя треугольная матрица:")
for i in range(N):
    for j in range(N):
        if i >= j:
            print(A[i][j], end=" ")
        else:
            print(" ", end=" ")  # Можно выводить пробелы вместо значений выше главной диагонали
    print()
