l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello', 4, 6, 7, 'g']
repeat_elem = []
for e in l:
    if l.count(e) > 1 and e not in repeat_elem:
        repeat_elem.append(e)
print(repeat_elem)
