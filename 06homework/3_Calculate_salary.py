entered_str = list(map(int, input().split()))
num_str = [int(i) for i in entered_str]
summ = 0
for i in range(len(num_str)):
    summ += num_str[i]
print('Средняя годовая зарплата', summ)