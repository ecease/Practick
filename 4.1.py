# Кондратюк Егор 3ИСд-1.22
# Практическая №4 Вариант 8
#Проверить утверждение о том, что результатами вычислений по формуле х2+ х +
#17 при 0 <= х <= 15 являются простые числа. Все результаты вывести на экран







def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for x in range(16):
    value = x**2 + x + 17
    print(f"x = {x}, значение = {value}, простое ли? {is_prime(value)}")
