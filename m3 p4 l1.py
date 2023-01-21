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
if ans == 'да':
    login, passwd = input('Введите логин: '), input('Введите пароль: ')
    register(login, passwd)




