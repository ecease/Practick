# Кондратюк Егор 3ИСд-1.22
# Практическая №10 Вариант 16
#Найти максимальный элемент среди упорядоченных либо по возрастанию, либо по убыванию строк заданной матрицы.






# размер матриц
N = int(input("Введите размер матрицы N: "))

# Счит исход матриц
A = []
print("Введите матрицу построчно:")
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# Сорт строк по возраст ( по сум элемент строк)
A_sorted_asc = sorted(A, key=sum)

# Сорт строк по убыв
A_sorted_desc = sorted(A, key=sum, reverse=True)

# Наход макс на глав диаг в вар по возраст
max_asc = A_sorted_asc[0][0]  # инициализ любым диагонал элемент
for i in range(N):
    if A_sorted_asc[i][i] > max_asc:
        max_asc = A_sorted_asc[i][i]

# Наход макс на глав диагонал в вар по убыв
max_desc = A_sorted_desc[0][0]
for i in range(N):
    if A_sorted_desc[i][i] > max_desc:
        max_desc = A_sorted_desc[i][i]


print("Макс элем глав диагонал при возраст строк:", max_asc)
print("Макс эле глав диагонал при убыв строк:", max_desc)
