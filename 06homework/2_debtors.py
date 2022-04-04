entered_str = list(map(int, input().split()))
num_str = [int(i) for i in entered_str]
for i in range(len(num_str)):
    if (num_str[i] > 0) and (num_str[i] % 2 == 0):
        print(num_str[i], '- Должник')
    else:
        print(num_str[i], '- Число не подходит')