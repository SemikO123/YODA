from random import *
import time
import sorts as s

def random_string(length):
    S = ''
    for i in range(length):
        S += chr(randint(30,100))
    return S

def random_simple_Array(N):
    Arr1 = [randint(0,1e+8)for i in range(N)]
    return Arr1

def random_extended_Array(N):           
    Arr1 = [[randint(0,1e+8),random_string(7),randint(0,100000)] for i in range(N)]
    return Arr1

def table(genFunction):
    print('{:^19}|{:^19}|{:^19}|{:^19}'.format('Кол-во элементов',\
                                    'Случайный массив','Упорядоченый',\
                                    'Упорядоченый в обратную сторону'))
    print('-'*76)
    Numbers = [1024,10000,50000]
    #Numbers = [5,10,20]
    for i in Numbers:
        A = genFunction(i)
        A_sorted = A[:]
        A_sorted.sort()
        A_invert = A[:]
        A_invert.sort(reverse = True)
        
        time0 = time.time()
        s.TimSort(A)
        time1 = time.time()-time0

        time0 = time.time()
        s.TimSort(A_sorted)
        time2 = time.time()-time0

        time0 = time.time()
        s.TimSort(A_invert)
        time3 = time.time()-time0
        
        print('{:^19d}|{:^19f}|{:^19f}|{:^19f}'.format(i,time1,time2,time3))
        print('-'*76)

print('{:^76}'.format('Обычный массив:'))
table(random_simple_Array)
print()

print('{:^76}'.format('Массив с дополнительными данными:'))
table(random_extended_Array)
print()

##K = random_extended_Array(100)
##for i in K:
##    print(i)

##time0 = time.time()
##L = random_simple_Array(40000)
##L.sort(reverse = True)
##flag = True
##for i in range(len(L)-1):
##    if L[i]<L[i+1]:
##        flag = False
##print('в обратную ',flag)
##
##s.TimSort(L)
##time1 = time.time()
##print('время %f'%(time1-time0))
##flag = True
##for i in range(len(L)-1):
##    if L[i]>L[i+1]:
##        flag = False
##print('отсортировано',flag)
