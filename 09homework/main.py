num = int(input('Введите число: '))
num_lst = []
for i in range(num//2):
    num_lst.append(2*i+1)
if num % 2 != 0:
    num_lst.append(num)
print('Список нечётных чисел от 1 до N:', num_lst)
