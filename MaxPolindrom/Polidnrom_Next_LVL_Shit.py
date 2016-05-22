from random import *
import time
#A = list(map(float,input().split()))
A = [randint(0,9) for i in range(
    int(input('Введите кол-во элементов массива : ')))]

time.clock()
'''for i in A:
    print(i, end=' ')
print()
print('Time from start = {:.6f}'.format(time.clock()))'''

Y1 = [0]*len(A)
Y2 = [0]*len(A)
L1 = L2 = -1
R1 = R2 = -1
for i in range(1, len(A)-1):
    if i > R1:
        x = 1
    else:
        x= min(A[L1+R1-i], R1-i) + 1
    while i-x >= 0 and i+x <= len(A)-1 and A[i-x] == A[i+x]:
        x += 1
    x -= 1 
    Y1[i] = x
    if i+x > R1:
        R1 = i+x
        L1 = i-x
        
    if i > R2:
        y = 1
    else:
        y = min(A[L2+R2-i], R2-i) + 1
    while i-y >= 0 and i+y-1 <= len(A)-1 and A[i-y] == A[i+y-1]:
        y += 1
    y -=1
    Y2[i] = y
    if i+y-1> R2:
        R2 = i+y-1
        L2 = i-y
if max(max(Y1), max(Y2)) == 0:
    print('No one polindrom has been found')
else:
    if max(Y1) >= max(Y2):
        MaxLen = max(Y1)
        Index = Y1.index(MaxLen)
        print(Index, MaxLen)
        print(A[Index-MaxLen:Index+MaxLen+1]) 
    else:
        MaxLen = max(Y2)
        Index = Y2.index(MaxLen)
        print(Index, MaxLen)
        print(A[Index-MaxLen:Index+MaxLen])         
print('Time from start = {:.6f}'.format(time.clock()))

    
