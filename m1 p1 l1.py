x, y, p = int(input()), int(input()), 1 + int(input()) * 0.01
years = 0
while x < y:
    years += 1
    x *= p
    x = round(x, 2)
print(years)