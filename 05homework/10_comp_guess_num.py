print('Загадайте число от 1 до 100')
counter = 0
N = 50
prev = 0
while True:
    state = int(input(f'Твое число равно,больше или меньше, чем {N}? '))
# 1 - равно, 2 - больше, 3 - меньше
    counter += 1
    a = abs((N - prev) // 2)
    prev = N
    if state == 1:
        break
    elif state == 2:
        N += a
    elif state == 3:
        N -= a
print(f'Это число: {N}')
print('Число попыток:', counter)
#zh