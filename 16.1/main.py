

# Подключаем функции из модуля factorial_module
from factorial_module import factorial, combinations

def main():
    # Считываем n и m
    n = int(input("Введите n: "))
    m = int(input("Введите m: "))
    
    
    fact_n = factorial(n)
    c_nm = combinations(n, m)
    
    # Выводим результаты
    print(f"Факториал {n} равен: {fact_n}")
    print(f"Число сочетаний C({n}, {m}) равно: {c_nm}")


main()
