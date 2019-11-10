def foo(s):
    s1 = []
    x = 1
    for i in s:
        for j in s:
            if i != j:
                x *= j
        s1.append(x)
        x = 1
    return(s1)


line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
print(foo(numbers))
