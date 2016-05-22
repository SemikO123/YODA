from math import *
b, St, c = map(float,input('Через пробел введите \
левую границу, шаг и правую границу отрезка : ').split())

Num_Of_Points = trunc((c-b)/St +1)
W = [0]*Num_Of_Points
X = [0]*Num_Of_Points
Curr = b

for i in range (Num_Of_Points):
    W[i] = Curr*Curr-1
    X[i] = Curr
    if -1.0e-10 < X[i] <1.0e-10:
        X[i] = 0
    Curr += St
    # Промежуточный вывод значений для наглядности
    # print(X[i],'\n',W[i],'\n','-'*20)

Fmax = max(W)
Fmin = min(W)

if Fmin >0 or Fmax < 0:
    Axis_Flag = False
else:
    Axis_Flag = True

Axis_Pos = round((0-Fmin) / (Fmax-Fmin) * 66)

print()
print('{:^67}{:^11}'.format('График функции W(x)', 'X:'))
for i in range(Num_Of_Points):
    
    Pos = round((W[i]-Fmin) / (Fmax-Fmin) * 66)
    
    if not Axis_Flag:
        print(' '*Pos, '*', ' '*(66-Pos), '{:^11g}'.format(X[i]), sep='')
        continue

    if Pos < Axis_Pos:
        print(' '*Pos, '*', ' '*(Axis_Pos - Pos - 1), '|', ' '*(66-Axis_Pos),
              '{:^11g}'.format(X[i]), sep='')
    elif Pos == Axis_Pos:
        print(' '*Pos, '*', ' '*(66-Pos),
              '{:^11g}'.format(X[i]), sep='')
    else:
        print(' '*Axis_Pos, '|', ' '*(Pos-Axis_Pos - 1), '*',  ' '*(66-Pos),
              '{:^11g}'.format(X[i]), sep='')
if Axis_Flag:
    print(' '*Axis_Pos, '|\n', ' '*Axis_Pos, 'V\n', ' '*Axis_Pos, 'X',sep='')
              
    

