import random
def get_id(id):
    i_skobka = id.index('(')
    return id[i_skobka + 1:]


def get_name(name_c, sex):
    letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Х', 'Э']
    name_sp = name_c.split(' ')
    fam = name_sp[0]
    if sex == 'м':
        name_new = name_sp[1][-2]
        papa = random.choice(letters)
    else:
        name_new = random.choice(letters)
        papa = random.choice(letters)
    s = fam + ' ' + name_new + '.' + papa + '.'
    return s


def get_number(phone):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    result = result + phone[:6]
    for i in range(7):
        result = result + random.choice(num)
    return result


def get_mail(pochta, sex):
    result = ''
    if sex == 'м':
        result = 'dad_of_' + pochta
    else:
        result = 'mom_of_' + pochta
    return result


with open('input.txt') as f:
    for line in f:
        line = line.strip().replace("'", "")
        stroka = line.split(', ')
        index = stroka[0]
        name = stroka[1]
        sex = stroka[2]
        date = stroka[3]
        clas = stroka[4]
        passport = stroka[5]
        phone = stroka[6]
        mail = stroka[7]
        street = stroka[8]
        house = stroka[9]
        app = stroka[10]
        ill = stroka[11]


        id_of_parent = get_id(index)
        name_of_parent = get_name(name, sex)
        child_of_parent = id_of_parent
        sex_of_parent = sex
        number_of_parent = get_number(phone)
        mail_of_parent = get_mail(mail, sex_of_parent)

        print(f"INSERT INTO parents VALUES ({id_of_parent}, '{name_of_parent}', '{sex_of_parent}', '{number_of_parent}', '{mail_of_parent}');")
