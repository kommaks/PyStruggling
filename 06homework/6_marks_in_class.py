N = int(input('Введите количество учеников:'))
num_lst = [int(input()) for i in range(N)]
threes = 0
fours = 0
fives = 0
for i in range(N):
    if num_lst[i] == 3:
        threes += 1
    elif num_lst[i] == 4:
        fours += 1
    elif num_lst[i] == 5:
        fives += 1
if (fives > threes) & (fives > fours):
    print('Отличников больше')
elif (fours > threes) & (fours > fives):
    print('Хорошистов больше')
else:
    print('Троечников больше')
