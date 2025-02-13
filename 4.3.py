import math

a = float(input("Введите начало отрезка a: "))  
b = float(input("Введите конец отрезка b: "))   
c = float(input("Введите шаг c: "))             

print("   x    |  F(x)")
print("-------------------")
x = a
while x <= b:
    try:
        d = math.cos(x) / math.sin(x)  # ctg(x)
        e = d + 1                      # F(x)
        print(f"{x:.3f} | {e:.3f}")
    except ZeroDivisionError:
        print(f"{x:.3f} | не определено")
    x += c