real_num = 7
counter = 0
while True:
    num = int(input('Введите число: '))
    counter += 1
    if num == real_num:
        break
    elif num < real_num:
        print('Число меньше, чем нужно. Попробуйте еще раз!')
    elif num > real_num:
        print('Число больше, чем нужно. Попробуйте еще раз!')
print('Вы угадали. Число попыток:', counter)
