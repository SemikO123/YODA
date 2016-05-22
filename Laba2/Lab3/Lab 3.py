''' Дано множество точек, провести окружность, проходящую как минимум через три
точки, такую что, разность между кол-вом точек внутри и снаружи окружности
было минимальным'''

# Далее следует очевидный фрагмент кода, не нуждающийся в пояснениях
def Circle(x1,y1,x2,y2,x3,y3):
    #Если не выполняется условие x1!=x2 and y1!=y2, то алгоритм не работает
    if x1 == x2 or y1 == y2:
        x2,x3,y2,y3 = x3,x2,y3,y2
    if x1 == x2 or y1 == y2:
        x1,x3,y1,y3 = x3,x1,y3,y1

    # (X-H)^2+(Y-V)^2=R^2
    #H = K*V+C, K,C- вычисляемыt коэффициентs
    K = (-2*y2+2*y1)/(-2*x1+2*x2)
    C = (x2**2 + y2**2 - x1**2 - y1**2)/(-2*x1 + 2*x2)

    V = ( (x3-C)**2 - (x2-C)**2 + y3**2 - y2**2)\
        /( 2*( (x3-C)*K - (x2-C)*K - y2 + y3) )
    H = K*V + C
    
    #sqRadius - квадрат радиуса
    sqRadius = (x1-H)**2+(y1-V)**2
    return H,V,sqRadius

#Ввод матрицы
def inputCoord():
    N = int(input('Введите количество точек: '))
    Arr1 = [0]*N
    Arr2 = [0]*N
    print('Введите координаты точек построчно через пробел: ')
    for i in range(N):
        Arr1[i],Arr2[i] = map(float, input().split())
    return Arr1, Arr2

#Вывод матрицы
def printCoord(Arr1, Arr2):
    print('Координаты точек :')
    for i in range(len(Arr1)):
        print('(%g;%g)' %(Arr1[i],Arr2[i]))

def printEquation(x0,y0,sqR):
    f = '{:.4g}'
    flag1,flag2 = True, True
    if x0 > 0:
        s1 = ' - '
    elif x0 < 0:
        s1 = ' + '
        x0 = abs(x0)
    else:
        flag1 = False
    if y0 > 0:
        s2 = ' - '
    elif y0 < 0:
        s2 = ' + '
        y0 = abs(y0)
    else:
        flag2 = False
    print('Окружность задается уравнением ',end='')
    if flag1:
        print('(x', s1, f.format(x0),')^2 + ', sep='', end='')
    else:
        print('x^2 + ', end='')
    if flag2:
        print('(y',s1,f.format(y0),')^2 ', sep='', end='')
    else:
        print('y^2', end='')
    print(' = ',f.format(sqR),sep='')
        

# Проверяем образуют ли точки прямую
def line(x1,y1,x2,y2,x3,y3):
    if (x3-x1)*(y2-y1) == (y3-y1)*(x2-x1):
        return True
    else:
        return False

# Проверяем входит ли точка в окружность
def inside(x0,y0,sqR,x1,y1):
    Vlen = (x1-x0)**2 + (y1-y0)**2
    if Vlen < sqR:
        return -1
    elif Vlen == sqR:
        return 0
    else:
        return 1
    
# *************************************************************

if input('Выполнить ввод с клавиатуры?(Enter для согласия/\'n\' для отмены)\
: ') == 'n':  
    X = [-5,-4,0,-1,0,0,2,4,5]
    Y = [3,0,4,1,5,-2,1,0,2]
    # X = [-4,0,-1,0,0,2,-5,4,5]
    # Y = [0,4,1,5,-2,1,3,0,2]
    # X = [1,2,3,4]
    # Y = [1,2,3,4]
else:
    X,Y = inputCoord()
printCoord(X,Y)

MinDiff = len(X);
CRCL = [0]*3
PNTS = [0]*3
for i in range(len(X)-2):
    for j in range(i+1,len(X)-1):
        for l in range(j+1,len(X)):
            if not line(X[i],Y[i],X[j],Y[j],X[l],Y[l]):
                curr = Circle(X[i],Y[i],X[j],Y[j],X[l],Y[l])
                insd = 0
                outsd = 0
                for p in range(len(X)):
                    if p!=i * p!=j * p!=l:
                        inflag = inside(curr[0],curr[1],curr[2],X[p],Y[p])
                        if inflag == -1:
                            insd += 1
                        elif inflag == 1:
                            outsd += 1
                if abs(insd - outsd) < MinDiff:
                    MinDiff = abs(insd-outsd)
                    CRCL = curr[:]
                    PNTS = [i,j,l]
                    '''printEquation(*CRCL)
                    print('(%g;%g)' %(X[i],Y[i]))
                    print('(%g;%g)' %(X[j],Y[j]))
                    print('(%g;%g)' %(X[l],Y[l]))
                    print('Снаружи %d Внутри %d' %(insd,outsd))'''
print()
if CRCL[2] == 0:
    print('Точки образуют прямую, провести окружность нельзя')
else:
    printEquation(*CRCL)
    print('И проходит через через точки :')
    print('(%g;%g)' %(X[PNTS[0]],Y[PNTS[0]]))
    print('(%g;%g)' %(X[PNTS[1]],Y[PNTS[1]]))
    print('(%g;%g)' %(X[PNTS[2]],Y[PNTS[2]]))











