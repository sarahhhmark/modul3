n = int(input())
total = 0
while n > 9:
    total += n % 10
    n //= 10
total += n
print(total)