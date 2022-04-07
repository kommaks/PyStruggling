text = input('Введите сообщение: ')
K = int(input('Введите сдвиг: '))
shifted = ''
a = ord('a')
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print(alphabet)
#получим строку 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(text)):
    if text[i] == ' ':
        shifted += ' '
    for l in range(len(alphabet)):
        if text[i] == alphabet[l]:
            if l + K < len(alphabet):
                shifted += alphabet[l + K]
            else:
                shifted += alphabet[l - len(alphabet) + K]
print('Зашифрованное сообщение:', shifted)

