a = int(input('Введите первое число:  '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if (a and b and c) != 0: print('Нет нулевых значений')

if (a or b or c) != 0:
    print('Первое ненулевое значение', (a or b or c)),
else:
    print('Ненулевых значений нет')

if a > (b + c): print(a - b - c),

if a < (b + c): print(b + c - a)

if a > 50 and (b > a or c > a): print('Вася')

if a > 5 or (b==7 and c==7): print('Петя')
