# Кондратюк Егор 3ИСд-1.22
# Практическая №10 Вариант 16
#Дана квадратная матрица порядка М. Повернуть ее в положительном направлении на 90°, 180° и 270°.






# Ввод размера матрицы
M = int(input("Введите размер матрицы M: "))

# Считываем матрицу
matrix = []
print("Введите матрицу построчно:")
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Поворот на 90° по часовой стрелке
matrix_90 = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        matrix_90[j][M-1-i] = matrix[i][j]

# Поворот на 180° по часовой стрелке
matrix_180 = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        matrix_180[M-1-i][M-1-j] = matrix[i][j]

# Поворот на 270° по часовой стрелке
matrix_270 = [[0]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        matrix_270[M-1-j][i] = matrix[i][j]

# Вывод результатов
print("\nИсходная матрица:")
for row in matrix:
    print(*row)

print("\nПоворот на 90°:")
for row in matrix_90:
    print(*row)

print("\nПоворот на 180°:")
for row in matrix_180:
    print(*row)

print("\nПоворот на 270°:")
for row in matrix_270:
    print(*row)
