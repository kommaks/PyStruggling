def num_pos(n):
    a, b = 1, 1
    for i in range(n - 2):
        a_temp = a
        a = b
        b += a_temp
    return b


place_of_num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', num_pos(place_of_num))