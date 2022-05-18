import math
volume_Earth = 10.8321*(10**11)
radius = float(input('Введите радиус случаной планеты: '))
volume_planet = 4/3 * math.pi * pow(radius, 3)    #pow()-возведение числа в степень
ratio = volume_Earth/volume_planet
if ratio > 1.0:
    print('Объем планеты Земля больше в', round(ratio, 3), 'раз')
else:
    print('Объем планеты Земля меньше в (1/' ,round(ratio, 3),  ')=', round(1/ratio, 3), ' раз', sep = '')