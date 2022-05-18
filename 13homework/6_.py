lowest = int(input('Нижняя граница: '))
highest = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('Вывод:')
celsium = [k for k in range(lowest, highest + 1, step)]
if (highest - lowest) % step != 0:
    celsium.append(highest)
fahrenheit = [int(round(i * 1.8 + 32)) if i >= 0 else int(round(i*1.8 - 32)) for i in (celsium)]
print('C', '\t', 'F')
for i in range(len(celsium)):
    print(celsium[i], '\t', fahrenheit[i] )