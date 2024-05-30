import random


def get_passport():
    res = ''
    for i in range(11):
        if i == 4:
            res = res + ' '
            continue
        res = res + str(random.randint(0, 9))
    return res


def get_phone_number():
    res = '+79'
    for i in range(9):
        res = res + str(random.randint(0, 9))

    return res


def get_date():
    res = '200'
    res = res + str(random.randint(5, 9))
    res = res + '-'
    res = res + str(random.randint(0, 1))
    if res[-1] == '1':
        res = res + str(random.randint(0, 2))
    else:
        res = res + str(random.randint(0, 9))
    res = res + '-'
    res = res + str(random.randint(0, 2))
    res = res + str(random.randint(0, 9))

    return res


def get_salary():
    res = ''
    res = res + str(random.randint(10, 50)) + '000'
    return int(res)


names = ['Арутюнян Г.А.', 'Батрунин Е.К.', 'Волкова И.Л.', 'Годрикова О.Н.', 'Дюнин М.М.', 'Егорова С.Л.', 'Ёршин П.А.',
         'Жалнин В.И.', 'Зубова К.В.', 'Иголкина Л.П.', 'Йошкаров Д.М.', 'Кравченко А.С.', 'Лапицкий А.Г.',
         'Макрицкий В.Д.',
         'Новиков К.А.', 'Осокина О.Я.', 'Пареева Г.Е.', 'Редкий Н.А.', 'Стойкина П.Н.', 'Туфлин Т.Д.', 'Уфимова А.А.',
         'Фалин М.С.',
         'Харитонова Е.Е.', 'Цискадзе Р.Н.', 'Чайка Е.Н.', 'Щевин Р.У.', 'Эфрон Ж.Г.', 'Юрова К.И.', 'Яшкин А.И.',
         'Абрикосова А.А.',
         'Бабаев Д.Н.', 'Васькина Г.П.', 'Гвоздичкина О.А.', 'Дуров Р.А.', 'Ерёменко О.О.', 'Ёршиков И.В.',
         'Жуликова О.В.',
         'Зябкина О.В.', 'Игнатьева Щ.В.', 'Йогн И.Б.', 'Кунавина Е.А.', 'Лефортова Ш.У.', 'Муртачева Г.Ф.',
         'Назарова Т.Е.',
         'Оганесян А.К.', 'Пройдёнова И.К.', 'Руденко С.Я.', 'Стопцева Г.П.', 'Тумаков О.В.', 'Ульянова Г.М.',
         'Фламингов Д.М.',
         'Хорькова И.И.', 'Целоусов Л.К.', 'Чашкина Г.Е.', 'Шапкин К.К.', 'Щукин Л.Н.', 'Эдуардов Э.Э.', 'Югансон Н.Е.',
         'Яковлев С.В.',
         'Авагян Г.А.', 'Бобров П.А.', 'Воинский Л.Л.', 'Главный Н.Г.', 'Дмитриев В.С.', 'Ельцин В.И.', 'Ёмкий Ш.Н.',
         'Жаркий Г.В.',
         'Зиновьева О.В.', 'Просицина У.П.', 'Ромашкина К.С.', 'Иголкина Н.К.', 'Коркин Н.Г.', 'Люстров Н.В.',
         'Мокрый Т.М.', 'Нуров И.С.',
         'Ольгина У.Ч.', 'Сестрицина О.С.', 'Табельников Д.С.', 'Уськина Д.А.', 'Фимченко И.В.', 'Хрюнин Ш.В.',
         'Цыганов Р.А.', 'Чехов Г.П.',
         'Шастун А.Н.', 'Щёчкин О.А.', 'Эриков О.А.', 'Юлов А.Г.', 'Ямайкин Д.Д.', 'Айрапетян Д.А.', 'Больнов М.М.',
         'Винный К.Б.',
         'Горюнов Д.М.', 'Деревянко М.В.', 'Емельянов А.А.', 'Ёриков С.С.', 'Жемчужина К.С.', 'Заика П.П.',
         'Илюшина И.М.', 'Кошкина О.К.',
         'Луспекян А.А.', 'Микоян А.Т.', 'Налбандян Л.И.']

mails = ['gaarutunyan@mail.ru', 'ekbatrunin@mail.ru', 'ilvolkova@mail.ru', 'ongodrikova@mail.ru', 'mmdunin@mail.ru',
         'slegorova@mail.ru',
         'paershin@mail.ru', 'vizhalnin@mail.ru', 'kvzubova@mail.ru', 'lpigolkina@mail.ru', 'dmioshkarov@mail.ru',
         'askravchenko@mail.ru',
         'aglapitskii@mail.ru', 'vdmakritskii@mail.ru', 'kanovikov@mail.ru', 'oyaosokina@mail.ru', 'gepareeva@mail.ru',
         'naredkii@mail.ru',
         'pnstoikina@mail.ru', 'tdtuflin@mail.ru', 'aaufimova@mail.ru', 'msfalin@mail.ru', 'eekharitonova@mail.ru',
         'rntsiskadze@mail.ru',
         'enchaika@mail.ru', 'rushevin@mail.ru', 'zhgefron@mail.ru', 'kiurova@mail.ru', 'aiyashkin@mail.ru',
         'aaabrikosova@mail.ru',
         'dnbabaev@mail.ru', 'gpvaskina@mail.ru', 'oagvozdichkina@mail.ru', 'radurov@mail.ru', 'ooeremenko@mail.ru',
         'ivershikov@mail.ru',
         'zhulikovaov@mail.ru', 'ovzyabrina@mail.ru', 'chvignatieva@mail.ru', 'ibiogn@mail.ru', 'enkunavina@mail.ru',
         'shulefortova@mail.ru',
         'gvmurtacheva@mail.ru', 'tenazarova@mail.ru', 'aloganesyan@mail.ru', 'ikproidenova@mail.ru',
         'syarudenko@mail.ru', 'gpstoptseva@mail.ru',
         'ovtumakov@mail.ru', 'gmulianov@mail.ru', 'dmflaminkov@mail.ru', 'iikhorkov@mail.ru', 'lktselousov@mail.ru',
         'gechashkina@mail.ru',
         'kkshapkin@mail.ru', 'lnshukin@mail.ru', 'eeeduardov@mail.ru', 'neuganson@mail.ru', 'svyakovlev@mail.ru',
         'gaavagyan@mail.ru',
         'pabobrov@mail.ru', 'llvoinskii@mail.ru', 'glavniing@mail.ru', 'vsdmitriev@mail.ru', 'vieltsin@mail.ru',
         'shnemkii@mail.ru',
         'gvzharkii@mail.ru', 'ovzinovieva@mail.ru', 'upprositsina@mail.ru', 'ksromashkina@mail.ru',
         'nkigolkina@mail.ru', 'ngkorkin@mail.ru',
         'nvlustrov@mail.ru', 'tmmokrii@mail.ru', 'isnurov@mail.ru', 'ucholgina@mail.ru', 'ossestritsina@mail.ru',
         'dstabelnikov@mail.ru',
         'dauskina@mail.ru', 'ivfimchenko@mail.ru', 'shvkrunin@mail.ru', 'ratsiganov@mail.ru', 'gpchekov@mail.ru',
         'anshastun@mail.ru',
         'oashechkin@mail.ru', 'oaerikov@mail.ru', 'agulov@mail.ru', 'ddyamaikin@mail.ru', 'daairapetian@mail.ru',
         'mmbolnov@mail.ru',
         'kbvinnii@mail.ru', 'dmgorunov@mail.ru', 'mvderevianko@mail.ru', 'aaemelianov@mail.ru', 'sserikov@mail.ru',
         'kszhemchuzhina@mail.ru',
         'ppzaika@mail.ru', 'imilushina@mail.ru', 'okkoshkina@mail.ru', 'aaluspekian@mail.ru', 'atmikoian@mail.ru',
         'linalbandyan@mail.ru']

addresses = ['ул. Южнобутовская, д.20, кв.181', 'ул. Ладожская, д.36, кв.98', 'ул. Ездаков, д.31, кв.33',
             'ул. Вятская, д.23, кв.160',
             'ул. Петровка, д.11, кв.204', 'ул. Камова, д.15, кв.450', 'ул. Константина Симонова, д.6, кв.353',
             'ул. Азовская, д.28, кв.341',
             'ул. Богданова, д.33, кв.65', 'ул. Новоорловская, д.35, кв.315', 'ул. Ездаков, д.6, кв.343',
             'ул. Бабаевская, д.28, кв.196',
             'ул. Ездаков, д.22, кв.406', 'ул. Машкова, д.14, кв.260', 'ул. Манежная, д.27, кв.446',
             'ул. Южнобутовская, д.45, кв.177',
             'ул. Бабаевская, д.9, кв.174', 'ул. Исаковского, д.9, кв.457', 'ул. Долгова, д.17, кв.236',
             'ул. Ефремова, д.41, кв.249',
             'ул. Братеевская, д.23, кв.332', 'ул. Константина Симонова, д.45, кв.449', 'ул. Волынская, д.23, кв.156',
             'ул. Погодинская, д.17, кв.274',
             'ул. Угличская, д.21, кв.215', 'ул. Дегтярная, д.40, кв.135', 'ул. Камова, д.27, кв.311',
             'ул. Гончарная, д.16, кв.423',
             'ул. Челябинская, д.36, кв.373', 'ул. Богданова, д.37, кв.147', 'ул. Бабаевская, д.31, кв.38',
             'ул. Изумрудная, д.41, кв.101',
             'ул. Набережная, д.31, кв.383', 'ул. Камова, д.8, кв.48', 'ул. Бахрушина, д.31, кв.267',
             'ул. Исаковского, д.1, кв.188',
             'ул. Камова, д.32, кв.425', 'ул. Мариупольская, д.19, кв.117', 'ул. Гончарная, д.4, кв.445',
             'ул. Чаплыгина, д.9, кв.441',
             'ул. Набережная, д.45, кв.196', 'ул. Челябинская, д.43, кв.460', 'ул. Юрьевская, д.20, кв.396',
             'ул. Малая Филёвская, д.20, кв.170',
             'ул. Зацепа, д.26, кв.137', 'ул. Удмуртская, д.32, кв.58', 'ул. Исаковского, д.4, кв.148',
             'ул. Волынская, д.34, кв.127',
             'ул. Бабаевская, д.13, кв.228', 'ул. Бабаевская, д.16, кв.200', 'ул. Кировоградская, д.9, кв.234',
             'ул. Бабаевская, д.37, кв.163',
             'ул. Бахрушина, д.45, кв.65', 'ул. Асеева, д.10, кв.176', 'ул. Житная, д.4, кв.62',
             'ул. Деловая, д.5, кв.88',
             'ул. Абельмановская, д.10, кв.372', 'ул. Малая Филёвская, д.43, кв.285', 'ул. Камова, д.43, кв.22',
             'ул. Прямикова, д.32, кв.395',
             'ул. Ладожская, д.26, кв.346', 'ул. Изумрудная, д.42, кв.22', 'ул. Молокова, д.13, кв.204',
             'ул. Авангардная, д.18, кв.368',
             'ул. Константина Симонова, д.27, кв.53', 'ул. Капотня, д.41, кв.354', 'ул. Заморёнова, д.16, кв.386',
             'ул. Петровка, д.18, кв.58',
             'ул. Константина Симонова, д.8, кв.40', 'ул. Автомоторная, д.13, кв.228',
             'ул. Абельмановская, д.6, кв.391',
             'ул. Кировоградская, д.29, кв.39', 'ул. Машкова, д.5, кв.439', 'ул. Озёрная, д.32, кв.432',
             'ул. Абельмановская, д.5, кв.183',
             'ул. Дегтярная, д.33, кв.14', 'ул. Мариупольская, д.5, кв.455', 'ул. Манежная, д.16, кв.104',
             'ул. Челябинская, д.32, кв.261',
             'ул. Автомоторная, д.29, кв.424', 'ул. Камова, д.23, кв.135', 'ул. Набережная, д.24, кв.99',
             'ул. Новоорловская, д.20, кв.114',
             'ул. Южнобутовская, д.33, кв.286', 'ул. Капотня, д.40, кв.19', 'ул. Манежная, д.10, кв.418',
             'ул. Набережная, д.11, кв.16',
             'ул. Челябинская, д.12, кв.42', 'ул. Озёрная, д.35, кв.224', 'ул. Амурская, д.9, кв.446',
             'ул. Зверинецкая, д.3, кв.64',
             'ул. Гагарина, д.5, кв.258', 'ул. Зверинецкая, д.22, кв.304', 'ул. Ездаков, д.20, кв.270',
             'ул. Пестеля, д.40, кв.283',
             'ул. Прямикова, д.1, кв.279', 'ул. Нижегородская, д.42, кв.128', 'ул. Волынская, д.16, кв.63',
             'ул. Удмуртская, д.13, кв.446',
             'ул. Волынская, д.15, кв.320', 'ул. Лобачика, д.19, кв.296', 'ул. Изумрудная, д.40, кв.201']

i = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip().replace("'", "")
        stroka = line.split(', ')
        index = stroka[0]
        scobka = index.index('(')
        clas = index[scobka + 1:]
        subjects = stroka[1]
        teacher_id = int(stroka[2])
        audition = int(stroka[3])
        amount_of_hours = int(stroka[4])
        exam = stroka[5]

        passport = get_passport()
        phone = get_phone_number()
        date = get_date()
        salary = get_salary()

        print(f"INSERT INTO supports VALUES ('{names[i]}', {teacher_id}, '{subjects}', '{clas}', '{passport}', '{phone}', '{mails[i]}', '{addresses[i]}', '{date}', {salary});")

        i += 1
