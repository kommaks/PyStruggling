positive_counter = 0
negative_counter = 0
while True:
    rating = int(input('Введите число:'))
    if rating == 0:
        break
    elif rating > 0:
        positive_counter += 1
    elif rating < 0:
        negative_counter += 1
print(negative_counter)
print(positive_counter)