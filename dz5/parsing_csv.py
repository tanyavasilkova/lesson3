headers = input("Файл содержит заголовки? (y/n)")
delim = input("Используемый разделитель: ")
result = {}
f = open(r'import.csv', 'r')
a = f.read().splitlines()
for item in a:
    slova = item.split(delim)
    result[slova[0]] = [slova[1], slova[2]]

#print(str(result.keys()[0]))

if headers == 'n':
    result.pop('id')



print(str(result))