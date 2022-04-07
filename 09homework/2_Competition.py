players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
choosen = []
for i in range(len(players)):
    if i % 2 == 0:
        choosen.append(players[i])
    else:
        continue
print(choosen)
