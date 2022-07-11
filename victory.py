kol = 0
koln= 0
vsego = 5

while True:
    otv = int(input ('Введите год рождения А.М. Ломоносова:'))
    if otv == 1711:
        kol = kol + 1
    elif otv != 1711:
        koln = koln + 1

    otv = int(input ('Введите год рождения Д.И. Менделеева:'))
    if otv == 1834:
        kol = kol + 1
    elif otv != 1834:
        koln = koln + 1

    otv = int(input('Введите год рождения С.В. Ковалевcкой:'))
    if otv == 1850:
        kol = kol + 1
    elif otv != 1850:
        koln = koln + 1

    otv = int(input('Введите год рождения А.Н. Колмогоров:'))
    if otv == 1903:
        kol = kol + 1
    elif otv != 1903:
        koln = koln + 1

    otv = int(input('Введите год рождения Н.И. Пирогов:'))
    if otv == 1810:
        kol = kol + 1
    elif otv != 1810:
        koln = koln + 1

    print(kol, 'правельных из', vsego)
    print(koln, 'ошибки из', vsego)
    procent = koln*100/vsego
    print(procent , 'неправильных' )

    if procent == 0.0:
        print('100% верных ответов! Генильно!До свидания!')
        break


    answer = input('Хотите продолжить? [да\нет]: ')
    if otv == 'да':
        print('Продолжим')
    elif otv == 'нет':
        print('Пока')








