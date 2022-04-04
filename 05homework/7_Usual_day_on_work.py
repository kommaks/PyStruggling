counter = 0
counter_of_taking = 0
print('Начался 8-часовой рабочий день')
for i in range(8):
    print(f'{i+1}-й час')
    #print(i+1, '-й час', sep ='')
    number_of_tasks = int(input('Сколько задач решит Максим? '))
    counter += number_of_tasks
    taking_phone = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    counter_of_taking += taking_phone
print('Рабочий день закончился. Всего выполнено задач:', counter)
if counter_of_taking != 0:
    print('Нужно зайти в магазин.')
