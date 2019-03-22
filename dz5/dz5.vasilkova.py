import json


def main():
    print('Выберите действие:\n\
          1. Зарегистрироваться\n\
          2. Войти')
    deistvie = str(input('Введите 1 либо 2: '))

    if deistvie == '1': registration();
    elif deistvie == '2': auth()
    elif deistvie != '1' or deistvie != '2':
        print('Вы ввели неверный символ!')
        return main()


def registration():  # регистрация
    login1 = str(input('Введите логин: '))
    password1 = str(input('Введите пароль: '))
    password2 = str(input('Повторите пароль: '))

    text = list(read_from_file())
    for item in text:

        if item['login'] != login1 and password1 != password2:  # проверка паролей
            print('Пароли не совпадают. Повторите ввод:'),
            return registration()

        if item['login'] == login1:  # проверка на отсутствие логина
            print('Такой логин уже существует, введите иной'),
            return registration()

        if item['login'] != login1 and password1 == password2:
            print('Вы успешно зарегистрированы. Вы вошли в систему. Меню:') # проверка условий логин-пароль и вход в систему
            info = data_bmi()
            log = {'login':login1, 'password':password1, 'data': info}


            text.append(log)
            write_to_file(text)

        menu()




def auth():  # войти по логину и паролю
    login = str(input('Login: '))
    password = str(input('Password: '))

    text = list(read_from_file())
    for item in text:

        if item['login'] != login:
            print('Ошибка! Введите верный логин либо зарегистрируйтесь!')
            return main()

        if item['login'] != login and item['password'] != password:
            print('Логин и пароль не совпадают. Повторите попытку либо зарегистрируйтесь!'),
            return main()

        if item['login'] == login and item['password'] == password:
            menu()



def menu():#  меню

    t = 0
    while t != 5:
        print('Выберите действие из возможных вариантов:\n\
        1. Вывести список пользователей\n\
        2. Добавить пользователя\n\
        3. Удалить пользователя\n\
        4. Выбрать пользователя\n\
        5. Выход')
        t = str(input('Введите число: '))

        if t == '1': viewusers();  # вывести список
        elif t == '2': data_bmi();  # добавить пользователя
        elif t == '3': deleteuser(); # удалить пользователя
        elif t == '4': selectuser();  # выбрать пользователя
        elif t == '5': print('Вы вышли из системы'), main()# выход на логин и пароль\регистрацию

        elif t !='1' or  t != '2' or t != '3' or t != '4' or t != '5': print('Неверно! ВВедите число от 1 до 5'),
        return menu()


def viewusers(): # посмотреть список пользователей
    print('Список пользователей:')

    text = list(read_from_file())
    for item in text:
        print(item['login'])


def data_bmi(): # добавить имя с данными

    a = str(input('Введите Ваше Имя: '))
    v = int(input('Введите Ваш возраст: '))
    while v < 18:
        print('Данное определение BMI предназначено для лиц старше 18 лет. Введите число больше 18.')
        v = int(input('Введите Ваш возраст: '))
    p = str(input("Если вы мужчина, укажите 'm', если женщина - 'w' "))
    while p != 'm' and p != 'w':
        print('Неверный ввод!')
        p = str(input("Если вы мужчина, укажите 'm', если женщина - 'w' "))
    r = float(input('Введите Ваш рост в сантиметрах: '))
    m = float(input('Введите Ваш вес в килограммах: '))
    description_bmi = bmi(a, v, p, r, m)

    d = {'Имя':a, 'Возраст':v,'Пол':p, 'Рост':r, 'Вес':m, 'BMI': description_bmi+'\n'}

    return d



def deleteuser(): # удалить имя с данными
    print('Выберите из списка Имя для удаления и введите его:')

    viewusers()
    del_user = str(input('Введите имя: '))

    text = list(read_from_file())
    for item in text:
        if item['login'] == del_user:
            text.remove(item)
            print('Введенный пользователь %s удален!' % del_user)
    write_to_file(text)

    return main()



def selectuser(): # посмотреть данные с именем

    print('Выберите из списка имя и введите его:')
    viewusers()
    imya_data = str(input('Введите имя: '))

    text = list(read_from_file())
    for item in text:
        if item['login'] == imya_data:
            print(item['data'])



def write_to_file(text):
    with open('userdb.txt', 'w') as outfile:
        json.dump(text, outfile)



def read_from_file():
    with open('userdb.txt', 'r') as outfile:
        return json.load(outfile)





def bmi(a, v, p, r, m): # функция bmi

    w = m / ((r ** 2) * 0.0001)
    w = float('{:.2f}'.format(w))

    if (p == 'w' and (((18 <= v < 31) and (w <= 16)) or (v >= 31 and w <= 17))) or \
            (p == 'm' and (((18 <= v < 31) and (w <= 18)) or (v >= 31 and w <= 19))):

        f = 'У вас наблюдается дифицит массы.\n\
            Оптимальный вес в соотвествии с вашим полом, возр   астом и ростом: 53.09-62.35 кг.\n\
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
        '0 %(resh)s %(BMI_w)d %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(number3)d' %
            {"resh": "#" * 5, "BMI_w": w, "resh": "#" * 5, "number1": 20, "prob": "_" * 15, "number2": 35, "star": "*" * 10, "number3": 45})

    if 20 <= w < 30: print(
        '0 %(resh)s %(number1)d  %(prob)s %(BMI_w)d %(prob)s %(number2)d %(star)s %(number3)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 5, "BMI_w": w, "prob": "_" * 5, "number2": 30, "star": "*" * 10, "number3": 40, "defis": "-" * 10})

    if 30 <= w < 40: print(
        '0 %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(BMI_w)d %(star)s %(number3)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 10, "number2": 30, "star": "*" * 5, "BMI_w": w, "star": "*" * 5, "number3": 40, "defis": "-" * 10})

    if w >= 40: print(
        '0 %(resh)s %(number1)d  %(prob)s %(number2)d %(star)s %(number3)d %(defis)s %(BMI_w)d %(defis)s' % {
            "resh": "#" * 10, "number1": 20, "prob": "_" * 10, "number2": 30, "star": "*" * 10, "number3": 40, "defis": "-" * 5, "BMI_w": w, "defis": "-" * 5})

    return str('Ваш BMI: ' + str(w))





main()
