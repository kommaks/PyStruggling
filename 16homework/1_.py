def generator(N):
    list = [i for i in range (1, N + 1)]
    string = ' '.join(str(a) for a in list)
    return string

num = int(input('Введите число: '))
print(generator(num))