salary = [int(input(f'Введите зарплату за {n + 1} месяц: ')) for n in range(10)]
i = 0
err = 0
while i < 9:
    if salary[i] < salary[i+1]:
        i += 1
    else:
        i = 10
        error = 0
if error == 0:
    print('Зарплаты не упорядочены по возрастанию')
else:
    print('Зарплаты увеличиваются каждый месяц. Все отлично')