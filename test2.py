data_users = {}

log_pass = {}

def main():

    print('Выберите действие:\n\
          1. Зарегистрироваться\n\
          2. Войти')
    deistvie = str(input('Введите 1 либо 2: '))

    def loginpassword():
        fp = str(input('Введите логин: '))
        password = str(input('Введите пароль: '))
        password2 = str(input('Повторите пароль: '))

        if password == password2: log_pass[fp] = password,  # menu()
        elif password != password2: print('Пароли не совпадат. Повторите ввод:')
        return



    if deistvie == 1: loginpassword()


    #elif








main()