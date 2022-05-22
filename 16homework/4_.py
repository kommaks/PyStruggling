site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def searcher(dicti, key):
    if key in dicti:
        print('Его значение:', dicti[key])
    for value in dicti.values():
        if isinstance(value, dict):
            searcher(value, key)


entered_key = input('Введите ключ: ')
searcher(site, entered_key)
