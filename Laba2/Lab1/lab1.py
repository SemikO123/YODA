def inputArr():
    N,M=map(int,input('Введдите кол-во строк и столбцов через пробел: ').split())
    print('Введите элементы матрицы построчно и через пробел :')
    Arr = [[float(x) for x in input().split()] for i in range(N)]
    Lflag = True
    Pflag = False
    for i in Arr:
        for j in i:
            if j > 0:
                Pflag = True
        if len(i) != M:
            Lflag = False
    if not Lflag * Pflag:
        print('Неверно введены данные, повторите ввод!')
        return inputArr()
    return Arr

def printArr(Arr):
    for i in Arr:
        for j in i:
            print('{:<8.4g}'.format(j), end=' ')
        print()
    print()

def Multiplication(X):
    p = 1
    for i in X:
        p *= i
    if len(X) == 0:
        p = -1;
    return p

def getMult(Arr):
    MultArr = [Multiplication([x for x in i if x > 0]) for i in Arr]
    
    return MultArr;

def getMin(Arr):
    Array = getMult(Arr)
    Min = Array.index(min([x for x in Array if x > 0]))
    return Min

def getMax(Arr):
    Array = getMult(Arr)
    Max = Array.index(max([x for x in Array if x > 0]))
    return Max

def LineDelete(Arr, Ind):
    Arr = Arr[:Ind] + Arr[Ind+1:]
    return Arr

# Основная программа
Z = inputArr()
print('Исходная Матрица :')
printArr(Z)

Z[getMax(Z)],Z[len(Z)-1] = Z[len(Z)-1],Z[getMax(Z)]
Z = LineDelete(Z, getMin(Z));

print('Сформированная матрица:')
printArr(Z)
