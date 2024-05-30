import random

with open('input.txt') as f:
    for line in f:
        line = line.strip().replace("'", "")
        stroka = line.split(', ')
        indexi = stroka[0]
        scob = indexi.index('(')
        id = indexi[scob + 1:]
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

        s = []
        result = []
        for i in range(12):
            dec_numbers = ['2', '3', '4', '5']
            a = random.choice(dec_numbers)
            if a == '2':
                b = random.choice(['8', '9'])
                c = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
            elif a == '5':
                b = '0'
                c = '0'
            else:
                b = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
                c = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

            res = a + '.' + b + c
            result.append(res)
        print(f"INSERT INTO statement VALUES ({id}, '{clas}', '{name}', {result[0]}, {result[1]}, {result[2]}, {result[3]}, {result[4]}, {result[5]}, "
              f"{result[6]}, {result[7]}, {result[8]}, {result[9]}, {result[10]}, {result[11]}, NULL);")
