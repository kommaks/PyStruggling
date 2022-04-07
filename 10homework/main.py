text = input('Введите текст: ')
lst = []
#lst = [] - пустой список
for i in range(len(text)):
    for l in ('а', 'о', 'у', 'е', 'ы', 'э', 'я', 'и', 'ю', 'ё'):
        if text[i] == l:
            lst.append(l)
print('Список гласных букв: ', lst)
print('Длина списка: ', len(lst))
