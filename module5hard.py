# Задание "Свой YouTube"

import time                                         # Импорт модуля time для реализации задержки времени


class User:
    """
    Класс User。 Для создания пользователей.
    """
    users = {}

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.users[nickname] = self.password

    def __repr__(self):
        return f'{self.nickname}'


class Video:
    """
    Класс Video。 Для создания записей о доступных видео.
    """
    videos = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    """
    Класс UrTube。 Основной класс, содержащий методы работы с пользователями и видео.
    """
    def __init__(self):
        self.users = User.users
        self.videos = Video.videos
        self.current_user = None
        self.current_video = None

    def register(self, nickname, password, age):            # Метод для регистрации пользователей
        if nickname in self.users:
            if hash(password) == self.users[nickname]:
                self.current_user = User(nickname, password, age)
            else:
                print(f'Пользователь {nickname} уже существует.')
        else:
            self.current_user = User(nickname, password, age)

    def log_in(self, nickname, password):                   # Метод для входа пользователей
        if nickname in self.users:
            if hash(password) == self.users[nickname]:
                self.current_user.nickname = nickname
            else:
                print(f'Неверный пароль для пользователя {nickname}.')
        else:
            print('Пользователь не найден.')

    def log_out(self):                                      # Метод для выхода пользователей
        self.current_user = None

    def add(self, *args):                                   # Метод для добавления нескольких видео в библиотеку
        for i in range(len(args)):
            if args[i] not in self.videos:
                self.videos.append(args[i])

    def get_videos(self, search_string):                    # Метод для проверки наличия видео в библиотеке
        match_list = []
        for i in range(len(self.videos)):
            compare_with = str(self.videos[i])
            if search_string.lower() in compare_with.lower():
                match_list.append(self.videos[i])
        return match_list

    def watch_video(self, video_title):                     # Метод для просмотра видео в библиотеке
        if v1.title == video_title:
            self.current_video = v1
        elif v2.title == video_title:
            self.current_video = v2
        else:
            print(f'Видео {video_title} не найдено.')
            return
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return
        elif self. current_video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет,пожалуйста покиньте страницу.')
            return
        print(f'Ролик - {self.current_video.title}\n')      # Симуляция воспроизведения видео
        playback_time = 0
        duration = self.current_video.duration
        width = 50
        while playback_time <= duration:
            percent = int(playback_time / duration * 100)
            left_side = width * percent // 100
            right_side = width - left_side
            print('\r[', '▓' * left_side, '-' * right_side, ']',
                  f'Воспроизведение: ', playback_time // 60, ':', playback_time % 60,
                  ' из ', duration // 60, ':', duration % 60,
                  f' - {percent}%', sep='', end='')
            time.sleep(0.1)
            playback_time += 1
            if percent == 100:
                print('\nВоспроизведение завершено.')


# Код для проверки работы
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
