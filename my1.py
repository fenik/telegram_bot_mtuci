import telebot
import requests
from telebot import types

token = "5254796526:AAF6CjFQlk_CXNhBu2r4djJIUPzMxlRBQ0U"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/weather", "/shutka", "/kino", "/games")
    bot.send_message(message.chat.id, 'Держу в курсе моих возможностей 🤗\n\n'
                                      'Мои команды: 🧐/help🧐\n☁Погода: /weather☁\n😅Анекдот: /shutka😅\n🍿Фильмы,'
                                      'сериалы: /kino🍿\n🎮Игры: /games🎮',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я умею: \n☁Рассказывать о погоде в москве☁ \nМогу анекдот рассказать 😅 \nПредложить фильмы, '
                     'сериалы🍿, игры🎮 на любой жанр')
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/weather", "/shutka", "/kino", "/games")
    bot.send_message(message.chat.id, "Вот мои команды", reply_markup=keyboard)


@bot.message_handler(commands=['weather'])
def weather(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Погода в Москве", "Погода в Москве на неделю")
    bot.send_message(message.chat.id, 'Какая сейчас погода?', reply_markup=keyboard)


@bot.message_handler(commands=['shutka'])
def shutka(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Нет", "Попробуй")
    bot.send_message(message.chat.id, 'Анекдодик?', reply_markup=keyboard)


@bot.message_handler(commands=['kino'])
def kino(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Фэнтези", "Боевик", "Триллеры", "Комедия", "Аниме")
    bot.send_message(message.chat.id, 'Какой жанр фильма вы хотите посмотреть?', reply_markup=keyboard)


@bot.message_handler(commands=['games'])
def games(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Стратегии", "РПГ", "Симулятор", "Головоломки", "Ужасы", "Гонки")
    bot.send_message(message.chat.id, '🤗 В какой жанр вы хотите поиграть?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "попробуй":
        bot.send_message(message.chat.id, 'Колобок повесился \nДа, не смешно, я всего лишь бот')
    elif message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'В другой раз😒')
        return start(message)
    elif message.text.lower() == "фэнтези":
        bot.send_message(message.chat.id, 'Фильмы серии "Властелин Колец"\n<https://yandex.ru/search/?clid=2358536'
                                          '&text=фильм+серии+властелин+колец+смотреть&l10n=ru&lr=213>\n\nТрилогия '
                                          'Гария '
                                          'Поттер\n<https://yandex.ru/search/?text'
                                          '=трилогия+гарри+поттер+смотреть+онлайн&lr=213&clid=2358536>\n\nСерия '
                                          '"Пираты Карибского '
                                          'моря"\n<https://yandex.ru/search/?text'
                                          '=пираты+карибского+моря+смотреть+онлайн&lr=213&clid=2358536>\n\nЕсли вам '
                                          'не понравилось, что я предложил, можете посмотреть туть👇', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '[inline URL](https://www.kinoafisha.info/rating/movies/fantasy/)',
                         parse_mode='Тыкай сюда!', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "боевик":
        bot.send_message(message.chat.id,
                         'Терминатор\n<https://yandex.ru/search/?text=терминатор+смотреть+онлайн&lr=213&clid=2358536'
                         '&src=suggest_B>\n\nДжентельмены\n<https://yandex.ru/search/?text'
                         '=джентльмены+смотреть+онлайн&lr=213&clid=2358536&src=suggest_W>\n\nГладиатор\n<https'
                         '://yandex.ru/search/?text=гладиатор+смотреть+онлайн&lr=213&clid=2358536&src=suggest_T>\n\n'
                         'Храброе сердце\n<https://yandex.ru/search/?text=храброе+сердце+смотреть+онлайн&lr=213&clid'
                         '=2358536>\n\nЕсли вам не понравилось, что я предложил, можете посмотреть '
                         'туть👇\n<https://www.kinoafisha.info/rating/movies/action/>', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '[inline URL](https://www.kinoafisha.info/rating/movies/action/)',
                         parse_mode='Тыкай сюда!', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "триллеры":
        bot.send_message(message.chat.id,
                         'Адвокат дьявола\n<https://yandex.ru/search/?clid=2358536&text'
                         '=адвокат+дьявола+смотреть+онлайн&l10n=ru&lr=213>\n\nКрестный '
                         'отец\n<https://yandex.ru/search/?text=крёстный+отец+смотреть+онлайн&lr=213&clid=2358536&src'
                         '=suggest_B>\n\nДом Gucci\n<https://yandex.ru/search/?text=дом+гуччи+смотреть+онлайн&lr=213'
                         '&clid=2358536&src=suggest_B>\n\nОстров '
                         'проклятых\n<https://yandex.ru/search/?text=остров+проклятых+смотреть+онлайн&lr=213&clid'
                         '=2358536&src=suggest_B>\n\nКод Да '
                         'Винчи\n<https://yandex.ru/search/?text=код+да+винчи+смотреть+онлайн&lr=213&clid=2358536>\n'
                         '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '[inline URL](https://www.kinoafisha.info/rating/movies/thriller/)',
                         parse_mode='Тыкай сюда!', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "комедия":
        bot.send_message(message.chat.id,
                         'Один дома\n<https://yandex.ru/search/?text=один+дома+смотреть+онлайн&lr=10719&clid=2358536'
                         '&src=suggest_B>\n\nОперация «Ы» и другие приключения '
                         'Шурика\n<https://yandex.ru/search/?text'
                         '=операция+ы+и+другие+приключения+шурика+смотреть+онлайн&lr=10719&clid=2358536&src=suggest_B'
                         '>\n\n1+1\n<https://yandex.ru/search/?text=1%2B1+смотреть+онлайн+&lr=10719&clid=2358536>\n\n'
                         'Форрест Гамп\nhttps://yandex.ru/search/?clid=2358536&text=форрест+гамп+смотреть+онлайн&l10n'
                         '=ru&lr=10719\n\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '[inline URL](https://www.kinoafisha.info/rating/movies/comedy/)',
                         parse_mode='Тыкай сюда!', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "аниме":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "стратегия":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "рпг":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "симулятор":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "головоломки":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "ужасы":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "гонки":
        bot.send_message(message.chat.id, 'Властелин Колец: Братство Кольца')
        return start(message)
    elif message.text.lower() == "погода в москве":
        bot.send_message(message.chat.id, weather_day())
        return start(message)
    elif message.text.lower() == "погода в москве на неделю":
        bot.send_message(message.chat.id, weather_week())
        return start(message)
    else:
        bot.send_message(message.chat.id, 'Для таких команд я ещё глуповат, вот меню')
        return start(message)


def weather_day():
    s_city = "Moscow,RU"
    appid = "0e79b59c56fc67936f82f0be0e5d5542"
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    weather_cond = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']

    weather_text = ''
    weather_text += f'Город🌎: {s_city}\n'
    weather_text += f'Погодные условия☁: {weather_cond}\n'
    weather_text += f'Температура🌡: {temp}\n'
    weather_text += f'Мин. температура: {temp_min}\n'
    weather_text += f'Макс. температура: {temp_max}\n'

    return weather_text


def weather_week():
    s_city = "Moscow,RU"
    appid = "0e79b59c56fc67936f82f0be0e5d5542"
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    week_weather = ''
    k = 0
    for i in data['list']:
        date = i['dt_txt']
        temp = i['main']['temp']
        weather_cond = i['weather'][0]['description']
        k += 1
        if k % 8 == 0:
            week_weather += f'Дата: {date}\n'
            week_weather += f'Температура🌡: {temp}\n'
            week_weather += f'Погодные условия☁: {weather_cond}\n\n'
    return week_weather


print('Бот запустился')
bot.polling(none_stop=True)
