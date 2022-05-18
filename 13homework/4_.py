number = float(input('Введите действительное число: '))
while number < 0:
    number = float(input(''))
res = (number - int(number))*10
print('Первая цифра после запятой: ', int(res))