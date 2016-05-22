def inputCoord():
    N = int(input('Введите количество точек: '))
    Arr1 = [0]*N
    Arr2 = [0]*N
    print('Введите координаты точек построчно через пробел: ')
    for i in range(N):
        Arr1[i],Arr2[i] = map(float, input().split())
    return Arr1, Arr2


def inputTr():
    N = int(input('Введите количество треугольников: '))
    Triangle = [[[0]*3,[0]*3] * N]
    for i in range(N):
        print('Введите координаты точек треугольника \
№%d построчно через пробел: ' %i)
        for j in range(3):
            Triangle[i][0][j],Triangle[i][1][j] = map(float, input().split())
    return Triangle

def per(x1,y1,x2,y2,x3,y3,x4,y4):
    if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
        return False
    
    if (x2-x1) == 0:
        if (x3 < x1 < x4) or (x3 > x1 > x4) :
            return True
        else:
            return False
    k1 = (y2-y1)/(x2-x1)

    if (x4-x3) == 0:
        Y = k1*x3 - k1*x1 + y1
        if (y3< Y< y4) or (y3> Y> y4):
            return True
        else:
            return False
    else:
        k2 = (y4-y3)/(x4-x3)
        X = (x1*k1-y1-x3*k2+y3)/(k1-k2)
        if (x3 < X < x4) or (x3 > X > x4):
            return True
        else:
            return False
def printequation(x1,y1,x2,y2):
    print('Уравнение прямой: ')
    if x1==x2:
        print('x = %g'%x1)
    elif y1 == y2:
        print('y = %g'%y1)
    else:
        k = (y2-y1)/(x2-x1)
        C = y1 - x1*k
        print('y = %g*X + (%g)'%(k,C))
          
#Tr = inputTr()
#A[0][1] = inputCoord();
#print(Tr)
        
#A = [[0,2,5,6],[-3,7,2,6]] 
#Tr = [[[-4,-1,2],[-1,3,-3]],[[2,4,6],[3,7,3]]]

A = [[0,4,4,8],[3,3.5,6,3]]
Tr = [[[2,4,6],[0,1,0]],[[2,4,6],[2,3,2]],[[2,4,6],[4,5,4]]]

#print(per(0,2,4,2,0,-2,3,4))
Max = 0
Ind1,Ind2 = 0,0
for i in range(len(A[0])-1):
    for j in range(i+1,len(A[0])):
        Curr = 0
        for k in range(len(Tr)):
            if per(A[0][i],A[1][i],A[0][j],A[1][j],Tr[k][0][0],
            Tr[k][1][0],Tr[k][0][1],Tr[k][1][1]) or per(A[0][i],
            A[1][i],A[0][j],A[1][j], Tr[k][0][1],Tr[k][1][1],Tr[k][0][2],
            Tr[k][1][2]) or per(A[0][i],A[1][i],A[0][j],A[1][j],Tr[k][0][2],
            Tr[k][1][2],Tr[k][0][0],Tr[k][1][0]) :
                Curr+=1
            
        if Curr > Max:
            Max,Ind1,Ind2 = Curr,i,j
print('Координаты точек :')
print('(%g;%g)' %(A[0][Ind1],A[1][Ind1]))
print('(%g;%g)' %(A[0][Ind2],A[1][Ind2]))
printequation(A[0][Ind1],A[1][Ind1],A[0][Ind2],A[1][Ind2])          
