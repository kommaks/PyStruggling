def Hanoi(N, start, stop):
    if N <= 0: return
    temp = 6 - start - stop
    Hanoi(N-1, start, temp)
    print('Transfer the disk ', N, 'from the rod', start, 'to the rod', stop)
    Hanoi(N-1, temp, stop)


amount = int(input('Enter the number of discs: '))
Hanoi(amount, 1, 3)
