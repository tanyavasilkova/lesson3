headers = input("Файл содержит заголовки? (д/н)")
delim = input("Используемый разделитель: ")
result = {}
f = open(r'import.csv', 'r')
a = f.read().splitlines()
for item in a:
    item.split(delim)
    result[item[0]] = [item[1], item[2]]

if headers == 'н':
    for i in a:


# парсинг тут
print(result)