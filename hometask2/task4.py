def combine(*a):
    d = a[0].copy()
    x = 0
    for i in a:
        if x == 0:
            x = 1
            continue
        for j in i:
            if j in d:
                d[j] = d[j]+i[j]
            else:
                d[j] = i[j]
    return d


d1 = {'a': 100, 'b': 200}
d2 = {'b': 300, 'c': 400}
d3 = {'a': 100, 'b': 500, 'd': 600}
print(combine(d1, d2))
print(combine(d1, d2, d3))
