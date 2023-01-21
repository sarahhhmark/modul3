d = {'a1': 'b1', 'a2': 'b2', 'a3':'b3'}
for k, v in d.items():
    d.pop(k)
    d[v] = k
print(d)
