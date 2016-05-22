from random import *
from math import *

def GetMSize(S):
    i = 0
    while i*i < len(S):
        i +=2
    return i

def rotate(i,j,A,x):
    n = len(A)
    for k in range(x):
        i,j = j,n-1-i
    return i,j

def GetBinary(Dec, Reverse = False):
    Bin = []
    while Dec > 0:
        if Reverse:
            Bin.append((Dec+1)%2)
        else:
            Bin.append((Dec)%2)    
        Dec = Dec//2
    Bin.reverse()
    return Bin

def GetQuadro(Dec,Size):
    Q = []
    while Dec > 0:
        Q.append(Dec%4)
        Dec = Dec//4
    Q.reverse()
    Q = [0]*(Size-len(Q))+Q
    return Q

#BArr - Basic Array
def GetBArr(A):
    n = len(A)
    for i in range(n//2):
        for j in range(n//2):
            Num = (n//2)*i+j+1
            A[i][j] = Num
            A[j][n-i-1] = Num
            A[n-i-1][n-j-1] = Num
            A[n-j-1][i] = Num

#BW - Black Whole 
def BWGen(A, ZeroOne = False):
    for i in range(len(A)//2):
        for j in range(len(A)//2):
            a,b = rotate(i,j,A,randint(0,3))
            A[a][b] = 0
    if ZeroOne:
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]!=0:
                    A[i][j] = 1

def BWGenNR(A,Rot):
    n = len(A)
    for i in range(len(A)//2):
        for j in range(len(A)//2):
            Num = (n//2)*i+j
            if Rot[Num] == 0:
                A[i][j] = 0
            else:
                a,b = rotate(i,j,A,Rot[Num])
                A[a][b] = 0

def TabGen(Tab,A,Str):
    for x in range(4):
        i,j = 0,0
        for leter in Str[x]:
            while A[i][j] != 0:
                j += 1
                if j == len(A):
                    j = 0
                    i += 1
            a,b = rotate(i,j,A,x)
            j += 1
            if j == len(A):
                j = 0
                i += 1
            Tab[a][b] = leter

def printMatr(A):
    for i in A:
        for j in i:
            print('{:<4}'.format(j),end=' ')
        print()
    print()

def printArr(A):
    for i in A:
        print(i)
    print()

def Dec(A):
    n = len(A)
    Dec = []
    for i in A:
        Curr = 0
        for j in range(len(i)):
            if i[j]== 0:
                Curr += 2**(n-j-1)
        Dec.append(Curr)
    return Dec


def GetBWFromDec(DArray,Size):
    Array = []
    for i in DArray:
        Bin = GetBinary(i, Reverse = True)
        Array.append([1]*(Size-len(Bin))+Bin)
    return Array

def GetText(Tab,Key):
    Text = ['']*4
    for i in range(len(Key)):
        for j in range(len(Key)):
            if Key[i][j] == 0:
                for x in range(4):
                    a,b = rotate(i,j,Tab,x)
                    Text[x]  += Tab[a][b]
    S = Text[0]+Text[1]+Text[2]+Text[3]
    return S

        


S = 'Меня очень расстраивает отсутствие моделя tkinder на моём компуктере,\
я бы пожаловался, но всем будет все равно на мою просьбу, поэтому я промолчу'
Size = GetMSize(S)
S = S + '%'*((Size)**2-len(S))
print('Исходная строка :')
print(S)
print()
Lena = (Size//2)**2
S = [S[:Lena],S[Lena:2*Lena],S[2*Lena:3*Lena],S[3*Lena:]]

A = [[0]*Size for i in range(Size)]


GetBArr(A)
printMatr(A)

BWGen(A, ZeroOne = True)
print('Ключ')
printMatr(A)

Tab = [[0]*Size for i in range(Size)]
TabGen(Tab,A,S)
print('Таблица')
printMatr(Tab)

Dec = Dec(A)
print('Десятичная интерпретация:')
printArr(Dec)

BWArray = GetBWFromDec(Dec,Size)
print('Востановленный ключ')
printMatr(BWArray)

print('Строка после дешифрации по ключу:')
print(GetText(Tab,BWArray))

##outfile = open('output.txt','w')
##
##TabForDec = [['т','ы','и','ь','с','р','а','м'],
##             ['я','л','о','л','н','о','ш','л'],
##             ['а','в','е','и','л','д','а','ш'],
##             ['г','у','л','я','о','с','и','е'],
##             ['т','и','ф','р','ц','ч','т','о'],
##             ['п','е','ь','а','в','т','е','п'],
##             ['с','р','и','у','л','и','д','р'],
##             ['к','а','т','ь','п','а','е','о']]
####TabForDec = Tab
##LenT = len(TabForDec)
##for i in range(4**((LenT//2)**2)):
##    rot = GetQuadro(i,(LenT//2)**2)
##    Rkey = [[1]*Size for i in range(Size)]
##    BWGenNR(Rkey,rot)
##    #rot = ' '.join(str(rot))
##    rot = str(rot)
##    outfile.write(GetText(TabForDec,Rkey)+rot+'\n')
##
##outfile.close()



        
