day_of_week = input('Введите день недели (с маленькой буквы): ')
num = 1
coincident = 0
for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
    if coincident == 0:
        if day_of_week != day:
            num += 1
        else:
            coincident = 1
print('Номер дня недели:', num)
