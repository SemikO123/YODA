from math import *
N0, St, N1  = map(float,input('Через пробел введите начальное \
значение, шаг и конечное значение параметра A : ').split())

Num_Of_Points = trunc((abs((N1 - N0) /St)+1 )) # Вычисляем кол-во точек
C1 = [' ']* Num_Of_Points
C2 = [' ']* Num_Of_Points
A = [' '] * Num_Of_Points
Curr = N0
In_Diap = 0 # In_Diap - кол-во точек входящий в заданный в условии диапазон

# Вывод таблицы
print()
print('{:^18}'.format('A'),'{:^18}'.format('C1'),'{:^18}'.format('C2'),sep='|')
print('-' * 57)
for i in range(Num_Of_Points):
    C1[i] = 4.05*pow(Curr,4)+12.6*pow(Curr,3)+8.8*pow(Curr,2)+11.2*Curr+17.7
    #C1[i] = cos(Curr)
    #C1[i] = 1/Curr
    #C1[i] = Curr
    #C1[i] = 5
    C2[i] = pow(Curr,2) + 4*sin(Curr)
    if -3 <= C1[i] and C1[i] <= 0:
        In_Diap += 1    
    A[i] = Curr
    if abs(A[i]) < 1e-7:
        A[i] = 0
    print('{:12.4g}      |{:12.4g}      |{:12.4g}      |'.\
          format(A[i],C1[i],C2[i]))
    print('-' * 57)
    Curr += St
print('Количество значений C1 попавших в диапазон [-3;0] =', In_Diap)  
print()
    
FMax = max(C1)
FMin = min(C1)

# Axis_Point - позиция оси OA на графике
if FMin != FMax:
    k = (0 - FMin) / (FMax - FMin)
    Axis_Point = round(66 * k)
else:
    Axis_Point = 33
    
# Axis_Flag - определяет требуется ли ось OA на графике
if (FMax != FMin and (FMax < 0 or FMin >0)):
    Axis_Flag = False
else:
    Axis_Flag = True
    
# Вывод графика      
print('{:^78}'.format('ГРАФИК ФУНКЦИИ C1(A)'))
print('{:^11}'.format('A :'))  
for i in range(Num_Of_Points):
    # Pos - позиция точки на графике, если график параллелен оси OA,
    # то выбирается середина между осью OX и границей графика
    if FMin != FMax:
        k = (C1[i] - FMin) / (FMax - FMin)
        Pos = round(66 * k)
    else:
        if FMax < 0:
            Pos = 16
        elif FMax == 0:
            Pos = 33
        else:
            Pos = 50
      
    if not Axis_Flag :
        print('{:^11}'.format( '{:.4g}'.format(A[i])),
              ' '*Pos, '*', ' '*(66-Pos), sep='')
        continue
    
    if Pos < Axis_Point:
        print('{:^11}'.format( '{:.4g}'.format(A[i])),
              ' '*Pos, '*', ' '*(Axis_Point-1-Pos), '|',
              ' '*(66-Axis_Point), sep='')
    elif Pos == Axis_Point:
        print('{:^11}'.format( '{:.4g}'.format(A[i])),
              ' '*Axis_Point, '*', ' '*(66-Axis_Point), sep='')
    elif Pos > Axis_Point:
        print('{:^11}'.format( '{:.4g}'.format(A[i])),
              ' '*Axis_Point, '|', ' '*(Pos-Axis_Point-1), '*',
              ' '*(66-Pos), sep='')
        
# Вывод направления оси OA(если требуется)
if Axis_Flag:
    print(' '*(Axis_Point+11),'|\n',
          ' '*(Axis_Point+11), 'V\n',
          ' '*(Axis_Point+11), 'A', sep='')

              
        
              
        
        
    
    








