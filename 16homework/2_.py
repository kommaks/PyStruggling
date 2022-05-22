def create_zip(obj1, obj2):
    new_lst = [*obj1, *obj2]
    another_new_lst = [(new_lst[i], new_lst[i+len(new_lst)//2]) for i in range(0, len(new_lst)//2)]
    return another_new_lst


string = 'abcd'
lst = ['f', 4, '*', -3.9]
tpl = (1, 2, 'g', '^')
set = {'Nastya', 2, '!', 'hehe'}
print(create_zip(tpl, lst))