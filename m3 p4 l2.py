import json
users = {'login1': 'passwd1'}
with open('users.json', 'w') as f:
    json.dump(users, f)

def register(login, passwd):
    with open('users.json', 'r') as f:
        users = json.load(f)

        with open('users.json', 'w') as f:
            users[login] = passwd
            json.dump(users, f)
    print(f'Вы успешно зарегистрированы!\nВаш логин: {login}\nВаш пароль: {passwd}')

ans = input('Желаете зарегистрироваться? ').lower()

while ans == 'да':
    login = input('Введите логин: ')
    def if_log_exist(login): #проверка на уникальность логина
        with open('users.json', 'r') as f:
            users = json.load(f)
            while login in users.keys():
                login = input('Пользователь с таким логином уже существует\nВведите другой логин: ')
            return login
    login = if_log_exist(login)
    passwd = input('Введите пароль: ')
    register(login, passwd)
    ans = input('Желаете зарегистрироваться? ').lower()




