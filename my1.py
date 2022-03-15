import telebot
import requests
import bs4
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
    bot.send_message(message.chat.id, 'Не забудте взять что-то похрумкать, выбирай жанр', reply_markup=keyboard)


@bot.message_handler(commands=['games'])
def games(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Стратегии", "РПГ", "Шутер", "Хоррор")
    bot.send_message(message.chat.id, 'Хм... вот лодари, выбирай жанр', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "попробуй":
        bot.send_message(message.chat.id, get_anek())
    elif message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'В другой раз😒')
        return start(message)
    elif message.text.lower() == "фэнтези":
        bot.send_message(message.chat.id,
                        '[Фильмы серии "Властелин Колец"](https://yandex.ru/search/?clid=2358536&text=фильм+серии+властелин+колец+смотреть&l10n=ru&lr=213)\n[Трилогия Гарри Потерра](https://yandex.ru/search/?text=трилогия+гарри+поттер+смотреть+онлайн&lr=213&clid=2358536)'
                        '\n[Серия Пираты Карибского моря](https://yandex.ru/search/?textпираты+карибского+моря+смотреть+онлайн&lr=213&clid=2358536)',
                        parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         'Если вам не понравилось, что я предложил, можете посмотреть туть👇\n[Тыкай сюда!](https://www.kinoafisha.info/rating/movies/fantasy/)\n[Фильм найти не может... тут ещё посмотри🤦‍♂️](https://www.kinopoisk.ru/lists/movies/genre--fantasy/?sort=votes&b=foreign)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "боевик":
        bot.send_message(message.chat.id,
                         '[Терминатор](https://yandex.ru/search/?text=терминатор+смотреть+онлайн&lr=213&clid=2358536&src=suggest_B)\n[Джентельмены](https://yandex.ru/search/?text=джентльмены+смотреть+онлайн&lr=213&clid=2358536&src=suggest_W)'
                         '\n[Гладиатор](https://yandex.ru/search/?text=гладиатор+смотреть+онлайн&lr=213&clid=2358536&src=suggest_T)\n[Храброе сердце](https://yandex.ru/search/?text=храброе+сердце+смотреть+онлайн&lr=213&clid=2358536)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         'Если вам не понравилось, что я предложил, можете посмотреть туть👇\n[Тыкай сюда!](https://www.kinoafisha.info/rating/movies/action/)\n[Фильм найти не может... тут ещё посмотри🤦‍♂️](https://www.kinopoisk.ru/lists/movies/genre--action/?sort=votes&b=high_rated)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "триллеры":
        bot.send_message(message.chat.id,
                         '[Адвокат дьявола](https://yandex.ru/search/?clid=2358536&text=адвокат+дьявола+смотреть+онлайн&l10n=ru&lr=10719)\n[Крестный отец](https://yandex.ru/search/?text=крёстный+отец+смотреть+онлайн&lr=213&clid=2358536&src'
                                          '=suggest_B)\n[Дом Gucci](https://yandex.ru/search/?text=дом+гуччи+смотреть+онлайн&lr=213)\n[Остров проклятых](https://yandex.ru/search/?text=остров+проклятых+смотреть+онлайн&lr=213&clid)\n[Код Да Винчки](https://yandex.ru/search/?text=код+да+винчи+смотреть+онлайн&lr=213&clid=2358536)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, 'Если вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://www.kinoafisha.info/rating/movies/thriller/)\n [Не нашел подходящий фильм?! Вот ещё](https://www.kinoafisha.info/rating/movies/thriller/)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "комедия":
        bot.send_message(message.chat.id,
                         '[Один дома](https://yandex.ru/search/?text=один+дома+смотреть+онлайн&lr=10719&clid=2358536&src=suggest_B)\n[Операция «Ы» и другие приключения Шурика](https://yandex.ru/search/?text=операция+ы+и+другие+приключения+шурика+смотреть+онлайн&lr=10719&clid=2358536&src=suggest_B)'
                         '\n[1+1](https://yandex.ru/search/?text=1%2B1+смотреть+онлайн+&lr=10719&clid=2358536)\n[Форрест Гамп](https://yandex.ru/search/?clid=2358536&text=форрест+гамп+смотреть+онлайн&l10n=ru&lr=10719)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         'Если вам не понравилось, что я предложил, можете посмотреть туть👇\n[Тыкай сюда!](https://www.kinoafisha.info/rating/movies/comedy/)\n['
                                          'Комедий навалом, вот ещё](https://www.kinopoisk.ru/lists/movies/genre--comedy/?sort=votes)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "аниме":
        bot.send_message(message.chat.id,
                         '[Атака Титанов](https://yandex.ru/search/?clid=2358536&text'
                         '=атака+титанов+смотреть+онлайн&l10n=ru&lr=10719)\n[Доктор Стоун]('
                         'https://yandex.ru/search/?clid=2358536&text=доктор+стоун+смотреть+онлайн&l10n=ru&lr=10719) '
                         '\n[Магическая битва](https://yandex.ru/search/?clid=2358536&text'
                         '=магическая+битва+смотреть+онлайн&l10n=ru&lr=10719)\n[Ванпанчмен]('
                         'https://yandex.ru/search/?clid=2358536&text=ванпанчмен+смотреть+онлайн&l10n=ru)\n[Клинок, '
                         'рассекающий демонов]('
                         'https://yandex.ru/search/?text=клинок+рассекающий+демонов+смотреть+онлайн&lr=10719&clid'
                         '=2358536)\n[Моя геройская академия]('
                         'https://yandex.ru/search/?clid=2358536&text=моя+геройская+академия+смотреть+онлайн&l10n=ru'
                         '&lr=10719)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://www.kinopoisk.ru/lists/movies/genre--anime/?sort=votes&b=high_rated&b=series)\n['
                                          'Посмотри ещё тут, авось найдешь](https://kg-portal.ru/anime/s_rating/)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "стратегии":
        bot.send_message(message.chat.id, '[Warhammer 40,000: Dawn of War](https://yandex.ru/search/?clid=2358536&text=Warhammer+40%2C000%3A+Dawn+of+War&l10n=ru&lr=10719)'
                         '\n[StarCraft II]('
                         'https://yandex.ru/search/?text=StarCraft+II&lr=10719&clid=2358536) '
                         '\n[Warcraft 3](https://yandex.ru/search/?text=Warcraft+3&lr=10719&clid=2358536)'
                         '\n[Civilization 6]'
                         '(https://yandex.ru/search/?text=Civilization+6&lr=10719&clid=2358536)\n[Crusader Kings II]'
                         '(https://yandex.ru/search/?text=Crusader+Kings+II&lr=10719&clid=2358536)'
                         '\n[Герои меча и магии 3]('
                         'https://yandex.ru/search/?text=Герои+меча+и+магии+3&lr=10719&clid=2358536)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://www.igromania.ru/games/all/strategy/)\n['
                                          'Не царское это дело, один источник давать, держи еще😘](https://m.moreigr.com/top-100-strategiy/)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "рпг":
        bot.send_message(message.chat.id,
                         '[The Elder Scrolls V: Skyrim](https://yandex.ru/search/?text=The+Elder+Scrolls+V%3A+Skyrim&lr=10719&clid=2358536&suggest_reqid=700340567162436735621088882529901)'
                         '\n[The Witcher 3: Wild Hunt]('
                         'https://yandex.ru/search/?clid=2358536&text=The+Witcher+3%3A+Wild+Hunt&l10n=ru&lr=10719) '
                         '\n[God of War](https://yandex.ru/search/?text=God+of+War&lr=10719&clid=2358536)'
                         '\n[Elden Ring]'
                         '(https://yandex.ru/search/?clid=2358536&text=Elden+Ring&l10n=ru&lr=10719)\n[World of Warcraft]'
                         '(https://yandex.ru/search/?clid=2358536&text=World+of+Warcraft&l10n=ru&lr=10719)'
                         '\n[Dark Souls 3](https://yandex.ru/search/?text=dark+souls+3&lr=10719&clid=2358536&src=suggest_Rec)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://mmo13.ru/games/top/ganre-382-RPG)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "шутер":
        bot.send_message(message.chat.id,
                         '[Half-Life 2](https://yandex.ru/search/?clid=2358536&text=Half-Life+2&l10n=ru&lr=10719)'
                         '\n[The Witcher 3: Wild Hunt]('
                         'https://yandex.ru/search/?clid=2358536&text=The+Witcher+3%3A+Wild+Hunt&l10n=ru&lr=10719) '
                         '\n[Серия Crysis](https://yandex.ru/search/?clid=2358536&text=Серия+Crysis&l10n=ru&lr=10719)'
                         '\n[Серия Call of Duty]'
                         '(https://yandex.ru/search/?text=серия+call+of+duty&lr=120126&clid=2358536&src=suggest_Reformulation)\n[Серия DOOM]'
                         '(https://yandex.ru/search/?clid=2358536&text=серия+doom&l10n=ru&lr=213)'
                         '\n[Серия Battlefield](https://yandex.ru/search/?text=Серия+Battlefield&lr=120126&clid=2358536)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://kanobu.ru/games/shooter/popular/)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "хоррор":
        bot.send_message(message.chat.id,
                         '[Серия Resident Evil](https://yandex.ru/search/?clid=2358536&text=Серия+Resident+Evil&l10n=ru&lr=10719)'
                         '\n[Серия The Dark Pictures Anthology]('
                         'https://yandex.ru/search/?text=серия+the+dark+pictures+anthology&lr=10719&clid=2358536&src=suggest_B) '
                         '\n[Серия Outlast](https://yandex.ru/search/?text=Серия+Outlast&lr=10719&clid=2358536)'
                         '\n[Alien: Isolation]'
                         '(https://yandex.ru/search/?clid=2358536&text=Alien%3A+Isolation&l10n=ru&lr=213)\n[Серия DOOM]'
                         '(https://yandex.ru/search/?clid=2358536&text=серия+doom&l10n=ru&lr=213)'
                         '\n[Серия Five Nights at Freddy](https://yandex.ru/search/?text=Серия+Five+Nights+at+Freddy%27s&lr=120126&clid=2358536)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, '\nЕсли вам не понравилось, что я предложил, можете посмотреть туть👇\n['
                                          'Тыкай сюда!](https://games.mail.ru/pc/games/compilation/luchshie-horrory-na-pk/)',
                         parse_mode='Markdown', disable_web_page_preview=True)
        return start(message)
    elif message.text.lower() == "погода в москве":
        bot.send_message(message.chat.id, weather_day())
        return start(message)
    elif message.text.lower() == "погода в москве на неделю":
        bot.send_message(message.chat.id, weather_week())
        return start(message)
    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать, вот меню')
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


def get_anek():
    z = ''
    s = requests.get('http://anekdotme.ru/random')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p = b.select('.anekdot_text')
    for x in p:
        s = (x.getText().strip())
        z = z + s + '\n\n'
    return s


print('Бот запустился')
bot.polling(none_stop=True)
