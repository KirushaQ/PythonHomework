def polindrom(s):
    x = s.replace(' ', '')
    if x == x[::-1]:
        return True
    return False


s = input()
print(polindrom(s))
