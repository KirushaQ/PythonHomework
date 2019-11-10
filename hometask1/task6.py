def long_word(s):
    s1 = s.split(' ')
    longest = 0
    longest_len = 0
    current_len = 0
    for i in s1:
        current_len = 0
        for j in i:
            current_len += 1
        if current_len > longest_len:
            longest_len = current_len
            longest = i
    return longest


s = input()
print(long_word(s))
