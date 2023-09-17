def printPat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            count = 0
            while count != i:
                print(j, end=' ')
                count += 1
        print('$', end='')
    print()

printPat(3)