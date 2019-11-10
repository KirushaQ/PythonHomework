def splt(s, ind):
    s1 = []
    s2 = ""
    for i in s:
        if i != ind:
            s2 += i
        else:
            s1.append(s2)
            s2 = ""
    if s2 != "":
        s1.append(s2)
    return s1


s = input()
ind = input()
print(splt(s,ind))