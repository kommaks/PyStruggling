a = [int(i) for i in input()]
#sum() суммирует эл-ты посл-сти iterable
if sum(a[:3]) == sum(a[3:]):
    print('lucky one :)')
else:
    print('unlucky ;(')

'''
a = int(input())
sum_left = 0
sum_right = 0
for i in range(6):
    if i<3:
        sum_right += a // 10**i % 10
    else:
        sum_left  += a // 10**i % 10
if sum_left == sum_right:
    print('lucky')
else:
    print('unlucky')  
'''