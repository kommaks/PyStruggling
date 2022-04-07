amount_of_debtors = int(input('Введите количество должников: '))
summ = 0
for i in range(amount_of_debtors // 5 + 1):
    print('Должник с номером', i * 5)
    debt = int(input('Сколько должны? '))
    summ += debt
print('Сумма долга:', summ)