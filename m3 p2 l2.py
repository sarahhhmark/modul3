from random import randrange
n = int(input())
m = [[randrange(100) for i in range(n)] for _ in range(n)]
max_num = 0
for i in range(n):
    if max_num < max(m[i]):
        max_num = max(m[i])
print(m)
print(max_num)