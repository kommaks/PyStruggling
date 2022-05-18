import math

amount_of_nums = int(input("Введите количество чисел:"))
for i in range(amount_of_nums):
    x = float(input("Введите число:"))
    if x < 0:
        print('x =', x, '\texp(x) =', math.exp(x))
    else:
        print('x =', x, '\tlog(x) =', math.log(x))