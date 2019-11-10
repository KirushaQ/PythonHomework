def pairs(s):
    if len(s) != 1:
        s1 = []
        s2 = ()
        a = 0
        s2 += (s[0],)
        for i in s:
            if a == 0:
                a = 1
                continue
            s2 += (i,)
            s1.append(s2)
            s2 = ()
            s2 += (i,)
        return s1


line = input()
words = line.split(' ')
print(pairs(words))
