def max_of_3(x, y, z):
    return max(max(x,y), max(y,z))

a, b, c = map(int, input('Введите 3 числа через пробел: ').split())
print (max_of_3(a, b, c))