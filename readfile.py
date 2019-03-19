log_pass = {'ww':'ee', 'ss':'dd'}

log = str(input('Введите логин: '))
password = str(input('Введите пароль: '))
password2 = str(input('Повторите пароль: '))

if log not in log_pass.keys() and password == password2:
    log_pass[log] = password,
    print(1),#, menu();
    log_pass[log] = password;
    print(log_pass)

