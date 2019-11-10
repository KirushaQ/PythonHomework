def generate_squares(a):
    d = {}
    for i in range(a):
        d[i+1] = (i+1)*(i+1)
    return d


a = input()
print(generate_squares(int(a)))
