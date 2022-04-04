n = int(input("Введите число:"))
counter = 0
while(n > 0):
    counter = counter + 1
    n = n // 10
print("Количество цифр равно:", counter)
