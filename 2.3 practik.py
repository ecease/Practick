import math

a, b, c, d, e, f = map(float, input("Введите 6 рёбер через пробел: ").split())


p1 = (a + b + c) / 2
area1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - c))

p2 = (a + d + e) / 2
area2 = math.sqrt(p2 * (p2 - a) * (p2 - d) * (p2 - e))

p3 = (b + d + f) / 2
area3 = math.sqrt(p3 * (p3 - b) * (p3 - d) * (p3 - f))

p4 = (c + e + f) / 2
area4 = math.sqrt(p4 * (p4 - c) * (p4 - e) * (p4 - f))


has_duplicates = False
if math.isclose(area1, area2):
    has_duplicates = True
if math.isclose(area1, area3):
    has_duplicates = True
if math.isclose(area1, area4):
    has_duplicates = True
if math.isclose(area2, area3):
    has_duplicates = True
if math.isclose(area2, area4):
    has_duplicates = True
if math.isclose(area3, area4):
    has_duplicates = True

print("Результат:", has_duplicates)
