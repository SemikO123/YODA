N = int(input('Введите размерность матрицы : '))
print('Введите элементы матрицы построчно через пробел')
A = [[x for x in input().split()] for i in range(N)]
print()

for i in A:
    for j in i:
        print('{:4}'.format(j), end='')
    print()
print()

for i in range(N//2 + N%2):
    for j in range(N//2):
        A[i][j],A[j][N-1-i],A[N-1-i][N-1-j],A[N-1-j][i] =\
        A[N-1-j][i],A[i][j],A[j][N-1-i],A[N-1-i][N-1-j]

for i in A:
    for j in i:
        print('{:4}'.format(j), end='')
    print()

