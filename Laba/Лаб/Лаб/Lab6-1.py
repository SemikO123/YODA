# В комментарии ниже представлен ввод с клавиатуры
N = int(input('Введите размерностьо матрицы : '))
print('Введите элементы матрицы построчно через пробел')
X = [[int(x) for x in  input().split()] for i in range(N)]
print()
'''N = 8
X = [[0,0,0,0,0,0,0,0],
     [0,1,1,1,0,1,1,1],
     [0,1,0,1,0,1,0,1],
     [0,1,0,1,1,1,0,1],
     [0,1,0,0,0,0,0,1],
     [0,1,0,0,0,0,1,1],
     [0,1,1,1,1,1,1,0],
     [0,0,0,0,0,0,0,0]]
     
for i in X:
    for j in i:
        print(j, end=' ')
    print()
print()'''

NumOfZero = 0
for i in range(len(X)):
    for j in range(len(X[i])):
        # Если с каждой стороны от 0 находится хотя бы одна единица,
        # то этот ноль находится в области
        if  X[i][j] == 0 and X[i][0:j].count(1) * X[i][j:N].count(1) *\
        [X[Ind][j] for Ind in range(0,i)].count(1) *\
        [X[Ind][j] for Ind in range(i,N)].count(1) != 0:
            NumOfZero += 1
         
print('Количество нулей в области ограниченой единицами =', NumOfZero)
            
        

        
            
            
            


