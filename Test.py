from random import *
A = [randint(0,9) for i in range(int(input('Введите кол-во элементов : ')))]
Y1 = [0]*len(A)
Y2 = [0]*len(A)
R1 = R2 = -1
for i in A:
    print(i, end=' ')
print()    
for i in range(1,len(A)):
    if i > R1:
        x = 1
    else:
        x = min(A[R1+L1-i], R1-i) + 1
    while i-x >= 0 and i+x <= len(A)-1 and A[i-x] == A[i+x]:
        x += 1
    x -= 1
    Y1[i] = x
    if i+x > R1:
        R1 = i+x
        L1 = i-x

    if i >R2:
        x = 1
    else:
        x = min(A[R2+L2-i], R2-i) + 1
    while i-x >= 0 and i+x-1 <= len(A)-1 and A[i-x] == A[i+x-1]:
        x += 1
    x -= 1
    Y2[i] = x
    if i+x-1 > R2:
        R2 = i+x-1
        L2 = i-x

MaxLen = max(max(Y1), max(Y2))
print(Y1,Y2, sep='\n')
print(MaxLen)
if not MaxLen == 0:
    if max(Y1) >= max(Y2):
        Index = Y1.index(MaxLen)
        print(A[Index-MaxLen:Index+MaxLen+1])
    else:
        Index = Y2.index(MaxLen)
        print(A[Index-MaxLen:Index+MaxLen])
else:
    print('No one polindrom has been found')
        
