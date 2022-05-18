def number10(num):
    count = 0
    while num > 10:
        num /= 10
        count += 1
    print('Формат плавающей точки: х =', num, '* 10 **', count)

def number1(num):
    count = 0
    while float(num) < 1:
        num *= 10
        count -= 1
    print('Формат плавающей точки: х =', num, '* 10 **', count)

num = float(input('Введите число: '))
if num > 1:
    number10(num)
elif num > 0:
    number1(num)
else:
    print('Ошибка ввода!')