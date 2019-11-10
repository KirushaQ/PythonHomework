def split_by_ind(s, ind):
    s1= []
    s2 = ""
    x = 0
    for i in range(len(s)):
        for x in ind:
            if i == x:
                s1.append(s2)
                s2 = ""
        s2 += s[i]
    if s2 != "":
        s1.append(s2)
    return s1


s = input()
line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
print(split_by_ind(s, numbers))