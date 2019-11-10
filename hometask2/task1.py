def string_1(a):
    x = 0
    set1 = set(a[0])
    for i in a:
        if x == 0:
            x = 1
            continue
        set2 = set(i)
        set1 = set1 & set2
    return set1


def string_2(a):
    x = 0
    set1 = set(a[0])
    for i in a:
        if x == 0:
            x = 1
            continue
        set2 = set(i)
        set1 = set1.union(set2)
    return set1


def string_3(a):
    x = 0
    set1 = set(a[0])
    set3 = set()
    for i in a:
        if x == 0:
            x = 1
            continue
        set2 = set(i)
        set3 = set3.union(set1 & set2)
        set1 = set2
    return set3


def string_4(a):
    x = 0
    set1 = set(a[0])
    alf = set('abcdefghijklmnopqrstuvwxyz')
    for i in a:
        if x == 0:
            x = 1
            continue
        set2 = set(i)
        set1 = set1.union(set2)
    return alf.difference(set1)


line = input()
strings = line.split(' ')
print(string_1(strings))
print(string_2(strings))
print(string_3(strings))
print(string_4(strings))
