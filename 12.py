def qsort(L):
    if L: return qsort([x for x in L if x<L[0]])\
       + [x for x in L if x==L[0]]\
       + qsort([x for x in L if x>L[0]])
    else:
        return[]
a=[4, 2, 5, 6]
qsort(a)
print(a)
