
c = 64  # общее количество лап
print("Возможные сочетания (a, b):")
for a in range(0, c // 4 + 1):  # a — кролики, b — гуси
    b = (c - 4 * a) // 2
    if b >= 0:
        print(f"Кролики (a): {a}, Гуси (b): {b}")