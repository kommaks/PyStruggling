X, Y, P = map(float, input().split())
#X - depo; P - year per cent; Y - needed amount of money
counter = 0
while X < Y:
    X = (X + 0.01 * P * X) // 1
    counter += 1
print(counter, 'лет')
