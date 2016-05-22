
#Печать массива
def printArr(Array):
    for i in Array:
        print(i,end = ' ')
    print() 

#Пузырёк)))
def buble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]

#TimSort
def TimSort(A): 
    # minrun - минимальный размер для упорядоченой последовательности
    def Getminrun(n):
        r = 0
        while n >= 64 :
            r = n % 2
            n >>= 1
        return n+r
    
    #Сортировка вставками
    def ins_sort(Array,left,right):
        for i in range(left+1,right):
            ind = i
            key = A[ind]
            while (key < A[ind-1]) and (ind > left) :
                A[ind]= A[ind-1]
                ind -= 1
            A[ind] = key
        return A

    # Слияние 2-х подмассивов на месте с выделением памяти под первый из них
    def merge(A,start1,len1,start2,len2):
        Arr = A[start1:start1+len1]
        # Индексы в исходном, а также 2-х временных подмассивах
        ind0,ind1,ind2 = start1,0,0
        while (ind1 < len1) and (ind2 < len2):
            if Arr[ind1]<=A[start2+ind2]:
                A[ind0] = Arr[ind1]
                ind1 += 1
            else:
                A[ind0] = A[start2+ind2]
                ind2 += 1
            ind0 += 1
        if ind1 < len1:
            A[ind0:start2+len2]=Arr[ind1:]
    
    minrun = Getminrun(len(A))
    #sub_Arrays - массив состоящий из начала и длины подмассивов
    sub_Arrays = []
    i = 0
    lenA = 1
    #Поиск упорядоченных подмассивов в исходном
    while i < len(A):
        while (i+lenA < len(A)) and (A[i+lenA] >= A[i+lenA-1]):
            lenA +=1
        if lenA < minrun :
            if i+minrun<len(A):
                lenA = minrun
            else:
                lenA = len(A)-i
        sub_Arrays.append([i,lenA])
        #Сортировка подмассива вставками
        ins_sort(A,i,i+lenA)
        
        i += lenA
        lenA = 1
    if len(sub_Arrays) == 1:
        return 0
    ind = 1
    while len(sub_Arrays)>2:
        if ind == len(sub_Arrays)-1:
            ind -= 1
        len1 = sub_Arrays[ind-1][1]
        len2 = sub_Arrays[ind][1]
        len3 = sub_Arrays[ind+1][1]
        
        if (len1 > (len2 + len3)) and (len2 > len3):
                ind +=1
                continue
        if len1 <= len3:
            merge_ind1 = ind-1
            merge_ind2 = ind        
        else:
            merge_ind1 = ind
            merge_ind2 = ind+1
                
        merge(A,*(sub_Arrays[merge_ind1]+sub_Arrays[merge_ind2]))
        new_start = sub_Arrays[merge_ind1][0]
        new_len = sub_Arrays[merge_ind1][1] + sub_Arrays[merge_ind2][1]
        sub_Arrays.insert(merge_ind1,[new_start,new_len])
        del(sub_Arrays[merge_ind2],sub_Arrays[merge_ind2])
    merge(A,*(sub_Arrays[0]+sub_Arrays[1]))






