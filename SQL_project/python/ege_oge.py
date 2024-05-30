import random

def get_score(subjects):
    res = []
    for i in subjects:
        res.append([i, random.randint(40, 100)])
    return res

with open('input.txt') as f:
    for line in f:
        line = line.strip().replace("'", "")
        stroka = line.split(', ')
        index = stroka[0]
        scobka = index.index('(')
        id = int(index[scobka + 1:])
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

        subjects_soc_econom = ['математика', 'русский', 'обществознание', 'английский']
        subjects_biohim = ['математика', 'русский', 'химия', 'биология']
        subjects_lang = ['математика', 'русский', 'английский', 'немецкий']

        if clas == '11А':
            scores = get_score(subjects_soc_econom)

        elif clas == '11Б':
            scores = get_score(subjects_lang)
        else:
            scores = get_score(subjects_biohim)

        for i in range(4):
            print(f"INSERT INTO exam_11 VALUES ({id}, '{clas}', '{scores[i][0]}', {scores[i][1]});")
