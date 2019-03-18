def main():
    print('Выберите действие из возможных вариантов:\n\
    1. Вывести список пользователей\n\
    2. Добавить пользователя\n\
    3. Удалить пользователя\n\
    4. Выбрать пользователя')
    t = int(input('Введите число: '))


    if t == 1: viewusers() #вывести список
    elif t == 2: adduser() #добавить
    elif t == 3: deleteuser() #удалить
    elif t == 4: selectuser() #выбрать пользователя

def viewusers():
    print('Список пользователей:')
    f = open(r'usersdata_f', 'r')
    usersdata = f.read().splitlines()
    for item in usersdata:
        print (item)



def adduser():
    f = open(r'usersdata_f', 'r')
    usersdata = f.read().splitlines()
    a = str(input('Введите Ваше Имя: '))
    v = int(input('Введите Ваш возраст: '))
    while v < 18:
        print('Данное определение BMI предназначено для лиц старше 18 лет. Введите число больше 18.')
        v = int(input('Введите Ваш возраст: '))

    p = str(input("Если вы мужчина, укажите 'm', если женщина - 'w' "))

    r = float(input('Введите Ваш рост в сантиметрах: '))
    m = float(input('Введите Ваш вес в килограммах: '))
    description_bmi = bmi(a, v, p, r, m)
    #usersdata.append(name)
    d = {a : {'age': v, 'sex': p, 'rost': r, 'ves': m, 'bmi': description_bmi+'\n'}}
    with open('usersdata_f', 'a') as out:
        for key, val in d.items():
            out.write('{}:{}\n'.format(key, val))

    f.close()



def deleteuser():
    viewusers()
    f = open(r'usersdata_f', 'r')
    usersdata = f.read().splitlines()
    print(usersdata)
    delete_user = str(input('\nВведите имя, которое хотите удалить: '))
    usersdata.remove(delete_user)

    f = open(r'usersdata_f', 'w')
    for item in usersdata:
        f.write('%s\n' % item.rstrip())

    f.close()




def selectuser():
    print('select  user')


def bmi(a, v, p, r, m):
    w = m / ((r ** 2) * 0.0001)
    w = float('{:.2f}'.format(w))

    if (p == 'w' and (((18 <= v < 31) and (w <= 16)) or (v >= 31 and w <= 17))) or \
            (p == 'm' and (((18 <= v < 31) and (w <= 18)) or (v >= 31 and w <= 19))):

        f = 'У вас наблюдается дифицит массы.\n\
        Оптимальный вес в соотвествии с вашим полом, возрастом и ростом: 53.09-62.35 кг.\n\
        Необходима коррекция питания.'

    elif (p == 'w' and (((18 <= v < 31) and (16 < w < 19.6)) or (v >= 31 and 17 < w < 20))) or \
            (p == 'm' and (((18 <= v < 31) and (18 < w < 21.5)) or (v >= 31 and 19 < w < 22))):

        f = 'У вас наблюдается недостаочная масса тела.\n\
        Оптимальный вес в соотвествии с вашим полом, возрастом и ростом: 53.09-62.35 кг.\n\
        Увеличьте калорийность рациона.'

    elif (p == 'w' and (((18 <= v < 31) and (19.6 <= w < 23)) or (v >= 31 and 20 <= w < 23.9))) or \
            (p == 'm' and (((18 <= v < 31) and (21, 6 <= w < 25)) or (v >= 31 and 22 <= w < 26))):
        f = 'У вас нормальный вес. Занимайтесь спортом и физической активностю,\n\
        ешьте больше овощей и фруктов, придерживайтель правильного питания. Будьте здоровы!'

    elif (p == 'w' and (((18 <= v < 31) and (23 <= w < 27.6)) or (v >= 31 and 23.9 <= w < 28))) or \
            (p == 'm' and (((18 <= v < 31) and (25 <= w < 29.6)) or (v >= 31 and 26 <= w < 30.1))):
        f = 'У вас избыточная масса тела.\n\
        Оптимальный вес в соотвествии с вашим полом, возрастом и ростом: 53.09-62.35 кг.\n\
        Скорректируйте свое питание: ограничьте потребление высококалорийных продуктов, увеличьте потребление\n\
        низкокалорийных продуктов (все виды зелени и овощи), фруктов и ягод.'

    elif (p == 'w' and (((18 <= v < 31) and (w >= 27.6)) or (v >= 31 and w >= 28.1))) or \
            (p == 'm' and (((18 <= v < 31) and (w >= 29.6)) or (v >= 31 and w >= 30.1))):
        f = 'У вас ожирение!\n\
        Оптимальный вес в соотвествии с вашим полом, возрастом и ростом: 53.09-62.35 кг.\n\
        Необходимо изменить образ жизни. Обратитесь к диетологу\n\
        для правильного составления рациона питания и физических нагрузок!'

    b = '\n Данные рекомендации носят приблизительный характер и не являются врачебным диагнозом.\n\
    Обратитесь к доктору за точным определением состояния здоровья  и назначением лечения, если \n\
    оно требуется. Расчет индекса масы тела в данном примере не подходит для спортсменов, беременных \n\
    женщин, подростков и детей.'

    if p == 'w':
        u = 'Уважаемая';
    elif p == 'm':
        u = 'Уважаемый '

    print(u, a, '!', 'Ваш возраст (в годах):', v, 'Ваш рост:', r, 'см', 'Ваш BMI:', w, f, b)


    print('График BMI')
    if w < 20: print(
        '0 %(resh)s %(BMI_w)d %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(number3)d' % {"resh": "#" * 5,
                                                                                                  "BMI_w": w,
                                                                                                  "resh": "#" * 5,
                                                                                                  "number1": 20,
                                                                                                  "prob": "_" * 15,
                                                                                                  "number2": 35,
                                                                                                  "star": "*" * 10,
                                                                                                  "number3": 45})

    if 20 <= w < 30: print(
        '0 %(resh)s %(number1)d  %(prob)s %(BMI_w)d %(prob)s %(number2)d %(star)s %(number3)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 5, "BMI_w": w, "prob": "_" * 5, "number2": 30,
            "star": "*" * 10,
            "number3": 40, "defis": "-" * 10})
    if 30 <= w < 40: print(
        '0 %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(BMI_w)d %(star)s %(number3)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 10, "number2": 30, "star": "*" * 5, "BMI_w": w,
            "star": "*" * 5,
            "number3": 40, "defis": "-" * 10})
    if w >= 40: print(
        '0 %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(number3)d %(defis)s %(BMI_w)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 10, "number2": 30, "star": "*" * 10, "number3": 40,
            "defis": "-" * 5,
            "BMI_w": w, "defis": "-" * 5})

    return str('Ваш BMI: '+ str(w))






main()
