a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
summ = 0
amount_of_num = 0
for i in range(a, b+1):
    if i % 3 == 0:
        summ += i
        amount_of_num += 1
print('Среднее арифметическое чисел равно:', summ / amount_of_num)