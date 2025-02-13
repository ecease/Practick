import math
x=int(input("Введите x: "))
y=int(input("Введите y: "))
one=x-10*math.sin(x)+abs(x**4-x**5)
two=x-10**math.sin(x)+math.cos(x-y)
print(one)
print(two)
