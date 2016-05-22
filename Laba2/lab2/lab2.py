def inputArr():
    L= int(input('Введдите размерность матрицы: '))
    print('Введите элементы матрицы построчно и через пробел :')
    Arr = [[x for x in input().split()] for i in range(L)]
    Lflag = True
    for i in Arr:
        if len(i) != L:
            Lflag = False
    if not Lflag :
        print('Неверно введены данные, повторите ввод!')
        return inputArr()
    return Arr

def printArr(Arr):
    for i in Arr:
        for j in i:
            print(j, end=' ')
        print()
    print()

def getSize(Arr, Ind1, Ind2):
    h,v = 1,1
    while Ind2+h < len(Arr[0]) and Arr[Ind1][Ind2+h] == 't': 
        h += 1
    while Ind1+v < len(Arr) and Arr[Ind1+v][Ind2] =='t':
        v += 1
    for i in range(v):
        for j in range(h):
            Arr[Ind1+i][Ind2+j] = 'z'
    return h*v
        

def MaxSizeCoord(Arr):
    x,y = 0,0
    maxArea = 0
    for i in range(len(Arr)):
        for j in range(len(Arr[0])):
            if Arr[i][j] =='t':
                currSize = getSize(Z,i,j)
                if currSize > maxArea:
                    maxArea,x,y = currSize,i,j
    return x+1,y+1

        
#Z = inputArr()
Z = [['t','f','f','f','f'],
     ['f','f','f','f','t'],
     ['f','t','t','f','t'],
     ['f','t','t','f','f'],
     ['f','t','t','f','f',]]
print('Матрица:')
printArr(Z)
C = MaxSizeCoord(Z)
print('Координаты верхнего левого угла наибольнего прямоугольника:',C[0],C[1])

