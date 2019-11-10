import operator


def get_top_students(path, number):
    text = open(path)
    a = 0
    lines = []
    for i in text:
        if a == 0:
            a = 1
            continue
        lines.append(i.replace('\n', ''))
    words_dict = {}
    a = 0
    for i in lines:
        x = i.split(';')
        words_dict[a] = x[2]
        a += 1
    sorted_lines = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    result = []
    for i in range(number):
        result.append(lines[(sorted_lines[i])[0]])
    text.close()
    return result


def sort_by_age(path):
    text = open(path)
    a = 0
    lines = []
    for i in text:
        if a == 0:
            a = 1
            continue
        lines.append(i.replace('\n', ''))
    words_dict = {}
    a = 0
    for i in lines:
        x = i.split(';')
        words_dict[a] = x[1]
        a += 1
    sorted_lines = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    result = []
    for i in range(len(lines)):
        result.append(lines[(sorted_lines[i])[0]])
    text.close()
    text = open('students_sorted.csv', 'w')
    text.write('student name;age;mark\n')
    for i in result:
        text.write(i + '\n')
        text.close()
    return result


print(get_top_students("students.csv", 10))
sort_by_age('students.csv')
