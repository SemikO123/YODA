from random import *
import time
#A = list(map(float,input().split()))
A = [randint(0,10) for i in range(
    int(input('Введите кол-во элементов массива : ')))]

time.clock()
'''for i in A:
    print(i, end=' ')
print()
print('Time from start = {:.6f}'.format(time.clock()))'''

MaxLen = 0
Pos0 = -1
Pos1 = -1

for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        Slice = [x for x in A[i:j+1]]
        Slice.reverse()
        if A[i:j+1] == Slice and len(A[i:j+1]) > MaxLen:
            # print('BINGO')
            MaxLen = len(A[i:j+1])
            Pos0 = i
            
print('Time from start = {:.6f}'.format(time.clock()))

if Pos0 != -1:
    print('Max Length = %d' % MaxLen, A[Pos0:Pos0+MaxLen], sep='\n')
else:
    print('No one polyndrom has been found')
