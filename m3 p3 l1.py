def area(a, b, c):
    p = (a + b + c) / 2
    return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)

a, b, c = 4, 5, 6
print(area(a, b, c))
