def rep(s):
    s1 = ""
    for i in s:
        if i != '\"':
            s1 += i
        else:
            s1 += '\''
    return s1


s = input()
s = rep(s)
print(s)