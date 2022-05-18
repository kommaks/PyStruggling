size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))
for i in range(size//speed):
    print('Прошло ', i+1, ' секунд. Скачано ', (i+1)*speed, ' из ', size, ' Мб (', int(round((i+1)*speed/size*100)), '%)', sep='')
if size % speed != 0:
    print('Прошло', size//speed + 1, 'секунд. Скачано', size, 'из', size, 'Мб (100%)')