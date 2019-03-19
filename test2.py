data_users = {}

log_pass = {}
def menu():
    t = str(input('Введите число: '))

    if t == '1':
        viewusers();  # вывести список
    elif t == '2':
        adduser();  # добавить пользователя
    elif t == '3':
        deleteuser();  # удалить пользователя
    elif t == '4':
        selectuser();  # выбрать пользователя
    elif t == '5':
        print('Вы вышли из симтемы'), main()  # выход на логин и пароль\регистрацию

    elif t != '1' or t != '2' or t != '3' or t != '4' or t != '5':
        print('Неверно! ВВедите число от 1 до 5'),
    return menu()




def main():

    print('Выберите действие:\n\
          1. Зарегистрироваться\n\
          2. Войти')
    deistvie = str(input('Введите 1 либо 2: '))

    if deistvie == '1': loginpassword();
    elif deistvie == '2': autint()
    elif deistvie != '1' or deistvie != '2': print('Вы ввели неверный символ!')


def loginpassword():  # регистрация
    log = str(input('Введите логин: '))
    password = str(input('Введите пароль: '))
    password2 = str(input('Повторите пароль: '))


    if log not in log_pass.keys() and password != password2:  # проверка паролей
        print('Пароли не совпадат. Повторите ввод:'),
        return loginpassword()

    if log in log_pass.keys():  # проверка на отсутствие логина
        print('Такой логин уже существует, введите иной'),
        return loginpassword()

    if log not in log_pass.keys() and password == password2: log_pass[log] = password, menu();  # проверка условий логин-пароль и вход в систему


def autint():  # войти по логину и паролю
    log2 = str(input('Login: '))
    password2 = str(input('Password: '))

    if log2 not in log_pass.keys():
        print('Ошибка! Введите верный логин либо зарегистрируйтесь!')
        return main()

    if password2 != log_pass[log2]:
        print('Логин и пароль не совпадают. Повторите попытку либо зарегистрируйтесь!'),
        return main()

    if password2 == log_pass[log2]:
        menu()



main()