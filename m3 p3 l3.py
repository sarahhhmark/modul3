from random import randint
s = [randint(1, 1000) for _ in range(10)] #генерируем 10 случайных чисел от 1 до 1000
print(s) #вывожу эти числа для того, чтобы можно было сравнить с результатом

def best_combination(s):
    s = [str(i) for i in s]
    res = ''
    def first_digit(n):
        return n[0]

    f_digits = set()

    for num in s:
        f = first_digit(num)
        f_digits.add(f)

    f_digits, s = sorted(list(f_digits), reverse=True), sorted(s, reverse=True)
    a = 0 #нижняя граница для вложенного цикла for
    for elem in f_digits:

        while elem in s:
            res += elem
            s.remove(elem)

        for j in range(a, len(s)):
            if elem == s[j][0]:
                res += s[j]
                a += 1 #увеличиваем нижнюю границу, чтобы при последующей итерации не проходится вновь по тем же числам
            else:
                break


    return res
print(best_combination(s))

