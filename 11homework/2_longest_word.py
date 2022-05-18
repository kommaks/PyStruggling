'''words = (input()).split(' ')
BiggestOne = max(words)
for i in range(len(BiggestOne)):
    i += 1
print(BiggestOne)
print(i)'''   #не вышло
s = input()
s = s.split()     #разбиение строки по разделителю
print('Самое длинное слово:', max(s, key=len), '\nДлина слова:', len(max(s, key=len)))
#max(iterable, key = func()), где key - ключевая функция, в которую передаются итерации, и выполняется сравнение на основе ее возвращаемого значения