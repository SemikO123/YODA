from random import *
def qSort(L):
    Num = randint(0,len(L))
    if L:
        return qSort([x for x in L if x < L[Num]]) + [x for x in L if x == L[Num]] \
               + qSort([x for x in L if x > L[Num]])
    return[]
