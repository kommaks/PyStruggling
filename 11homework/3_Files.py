s = input()
st_check_str = '@№$%^&*()'
for i in range(len(st_check_str)):
    if st_check_str[i] == s[0]:
        print('Ошибка: название начинается на один из специальных символов')
        break
    elif s.endswith('.txt') or s.endswith('.docx'):   #s.enwith('.txt') - pаканчивается ли строка s шаблоном '.txt'
        print('Файл назван верно.')
        break
    else:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        break