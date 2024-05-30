import random

def get_number():
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = '+79'
    for i in range(9):
        result = result + random.choice(num)
    return result

def get_passport():
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    for i in range(4):
        result = result + random.choice(num)
    result = result + ' '
    for i in range(4):
        result = result + random.choice(num)
    return result

anti_repeat = set()
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
        while True:
            phone_res = get_number()
            if phone_res in anti_repeat:
                continue
            else:
                anti_repeat.add(phone_res)
                break
        while True:
            passport_res = get_passport()
            if passport_res in anti_repeat:
                continue
            else:
                anti_repeat.add(phone_res)
                break

        print(f"{index}, '{name}', '{sex}', '{date}', '{clas}', '{passport_res}', '{phone_res}', '{mail}', '{street}', '{house}', '{app}', {ill}")
