a = list(map(int, input('Введите кол-ва дней в месяцах: ').split()))
counter = 0
for x in a:
    if x % 2 == 0:
        counter = counter + 1
    if x == 0:
        break
print(counter - 1)
#ломаный вывод количествав четных чисел при вводе через пробел

'''
counter = 0
print('Введите кол-ва дней в месяцах: ')
while True:
    number_of_days_in_month = int(input())
    if number_of_days_in_month == 0:
        break
    elif not number_of_days_in_month % 2:
        counter += 1
print(counter)
'''