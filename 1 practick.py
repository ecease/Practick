import math
S_original = int(input("Введите площадь исходного квадрата: "))
side_original = math.sqrt(S_original)
radius = side_original / 2
diagonal = 2 * radius
side_inscribed = diagonal / math.sqrt(2)
S_inscribed = side_inscribed ** 2
ratio = S_original / S_inscribed
print(S_inscribed)
print(ratio)
