N = int(input('Введите количество карточек:'))
num_of_card = [int(input(f'Введите номер карточки: ')) for i in range(N - 1)]
for i in num_of_card:
    if num_of_card[i] != i+1:
        num_of_lost_card = num_of_card[i]
        break
print('Номер потерянной карточки:', num_of_lost_card - 1)