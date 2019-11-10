text = open('unsorted.txt')
names = sorted(text.readlines())
text.close()
text = open('sorted.txt', 'w')
for i in names:
    text.write(i)
text.close()