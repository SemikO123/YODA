##from random import *
##import time
##
##def qsort(A,low,high):
##    l = low
##    r = high
##    N = A[randint(low,high)]
##    while l <= j:
##        while A[l] < N:
##            l += 1
##        while A[r] > N:
##            r -= 1
##        A[l],A[r] = A[r],A[l]
##        l += 1
##        r -=1
##    if r > low:
##        qsort(A,low,r)
##    if l < high:
##        qsort(A,l,high)
##
##        
##
##LEN = 100000
##A = [randint(0,100) for i in range(LEN)]
##time1 = time.time()
##A.sort()
##time2 = time.time()
##print('Время %.8f'%(time2-time1))

def swap(A,B):
    A,B = B,A
