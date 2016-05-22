from random import *
def qsort(List):
    if List:
        Num = randint(0,len(List)-1)
        return qsort([x for x in List if x < List[Num]]) \
               +[x for x in List if x == List[Num]] \
               + qsort([x for x in List if x > List[Num]])
    return[]


L = []

for i in range(int(input('Введите кол-во элементов : '))):
    L.append(randint(0,151)-50)
for i in L:
    print(i, end=' ')
print()
L = qsort(L)
for i in L:
    print(i, end=' ')


    
    
            
    
