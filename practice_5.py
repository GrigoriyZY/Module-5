# Практика к модулю %

class Database:
    """
    Класс базы данных пользователей
    """
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Клас пользователя содержащий аттрибуты: логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Логин\n2 - Регистрация\n3 - Выход\n'))
        if choice == 1:
            login = input('Введите логин:')
            password = input('Введите пароль:')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен пользователем {login}.')
                    break
                else:
                    print('Введен неверный пароль.')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input('Введите логин: '),
                        password1 := input('Введите пароль: '),
                        password2 := input('Повторите пароль:'))
            if password1 != password2:
                print('Пароль не совпадает. Попробуйте еще раз.')
                continue
            elif len(password1) < 8:
                print('Введенный пароль слишком короткий, придумайте другой.')
                continue
            elif password1.isalpha():
                print('Пароль должен содержать хотя бы одну цифру, придумайте новый.')
                continue
            elif password1.islower():
                print('Пароль должен содержать хотя бы один заглавный символ. Придумайте другой.')
                continue
            database.add_user(user.username, user.password)
        if choice == 3:
            break
