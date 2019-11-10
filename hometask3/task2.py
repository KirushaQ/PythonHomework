def find_most_common_words(path):
    text = open(path)
    words_dict = {}
    string = ''
    for i in text:
        string = string + ' ' + i.replace('\n', '')
    words = string.split(' ')
    max = 0
    res = []
    for i in words:
        if i in words_dict:
            words_dict[i] += 1
            if max < words_dict[i]:
                max = words_dict[i]
        else:
            words_dict[i] = 0
    for i in words_dict:
        if words_dict[i] == max:
            res.append(i)
    text.close()
    return res


print(find_most_common_words("common.txt"))
