N = int(input('Введите размерностьо матрицы : '))
print('Введите элементы матрицы построчно через пробел : ')
A = [[int(x) for x in input().split()] for i in range(N)]
print()

B = []
for i in range(N):
    B.append(A[i][0:i]+A[i][i+1:N])
    
for i in B:
    for j in i:
        print('{:^5d}'.format(j),end='')
    print()
print()

Ind_Max = -1
Max = 0
for i in range(N-1):
    Curr = 0
    for j in range(N):
        if B[j][i] > 0:
            Curr +=1
    if Curr > Max:
        Max = Curr
        Ind_Max = i
if Ind_Max == -1:
    print('В массиве B нет положительных элементов')
else:
    print('Номер столбца : {} \nКоличество положительных элементов : {}'.\
          format(Ind_Max, Max))
        
    
