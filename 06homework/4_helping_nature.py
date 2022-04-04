counter = 0
for i in (30, 31, 32, 33, 34, 35):
    people = int(input(f'Людей в {i}-м секторе: '))
    if people > 10:
        print('Нарушение! Слишком много людей в секторе!')
        counter += 1
    else:
        print('Всё спокойно')
print('Количество нарушений:', counter)