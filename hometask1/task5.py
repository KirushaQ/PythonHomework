def get_digits(x):
    s1 = []
    for i in str(x):
        s1.append(int(i))
    return s1


x = input()
print(get_digits(x))