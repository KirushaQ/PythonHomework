def count_letters(s):
    d = {}
    for i in s:
        d[i] = 0
    for i in s:
        if i in d:
            d[i] = d[i]+1
    return d


line = input()
print(count_letters(line))
