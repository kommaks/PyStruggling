#1
print('Hello World')
print('Hello World')
print("Hello World")
print("Hello")
print('Привет', '')
print('Меня зовут Вася')
print('и я умнее всех')
#2
print('----------')
print('|00000000|')
print('|00000000|')
print('|00000000|')
print('|00000000|')
print('----------')
#3
print( '='*30 )
print( 'Привет')
print( 'друг!')
print( '='*30 )

print( '='*30 )
print('||', ' '*9, end='')
print( 'Привет', ' '*8, '||')
print('||', ' '*9, end='')
print( 'друг!', ' '*9, '||')
print( '='*30 )

print( '='*30 )
print('||', ' '*24, '||')
print('||', ' '*24, '||')
print('||', ' '*9, end='')
print( 'Привет', ' '*8, '||')
print('||', ' '*9, end='')
print( 'друг!', ' '*9, '||')
print('||', ' '*24, '||')
print('||', ' '*24, '||')
print( '='*30 )
#4
client = 'Петя'
print(client)
print(' и ')
pet = 'Кот'
print(pet)
#5
r = 'Red'
g = 'Green'
b = 'Blue'
print(r, b, g, r + g + b, b, g + b)
#3
first_animal, second_animal = 'Hare', 'Turtle'
print( first_animal, 'sleeps,', second_animal, 'walks')
#4
print('Введите имя:', end = ' ')
#name = 'Максим'
#print(name)
name = input()
print('Введите фамилию:', end = ' ')
#surname = 'Комяков'
#print(surname)
surname = input()
print('Вас зовут:')
print(name)
print(surname)

print('Введите имя:', end = ' ')
name = input()
print('Введите фамилию:', end = ' ')
surname = input()
print('Введите город проживания:', end = ' ')
living_city = input()
print( '='*10 )
print('Вас зовут', name, surname)
print('Вы  живете в городе', living_city)
#5
first_name = input('Введите имя пользователя: ')
greeting = 'Привет,'
print(greeting, first_name)
intro = "К сожалению, у Вас нет доступа к системе."
info = "Пожалуйста, обратитесь к системному администратору."
print(intro)
print(info)
#6
print('Введите город вылета:', end = ' ')
#departing_city = "Нижний Новгород"
#print(departing_city)
departing_city = input()
print('Введите город прибытия:', end = ' ')
#arriving_city = "Москва"
#print(arriving_city)
arriving_city = input()
print(departing_city, "-", arriving_city)
#7
print('Введите пользователя:', end = ' ')
#user = "Maxim"
#print(user)
user = input()
print('Введите имя файла:', end = ' ')
#new_file = "Start1"
#print(new_file)
new_file = input()
print('C:/', user, '/docs/folder/', new_file, '.txt', sep = '')
#8
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
t =''
t = a
a = b
b = t
print(a, b)
