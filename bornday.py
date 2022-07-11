year = int(input('Введите год рождения А.С. Пушкина: '))

if year == 1799:
   day = (int(input('Введите его день рождения: ')))
   if day == 6:
       print('Верно')
   elif day != 6:
       print('Неверный день рождения')
elif year != 1799:
    print('Неверный год')

print('end')






