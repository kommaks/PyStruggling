lst = [i for i in range(10, 100)]
wonderful_list = []
for i in lst:
    num = (i//10) * (i % 10) * 3
    if i == num:
        wonderful_list.append(i)
print('Замечательными числами являются:', ', '.join(map(str, wonderful_list)))
# .append - добавить эл-т; .join - пробелы в списке
# map(тип_данных, название_строки или комманда)
