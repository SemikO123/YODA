A = input('Введите строку : ')
i = 0
while i < len(A):
    Chislo = 0
    if '0' <= A[i] <= '9':
        while i < len(A) and '0' <= A[i] <= '9' :
            Chislo =Chislo *10 + int(A[i])
            A = A[:i]+A[i+1:]
        if i > 0:

            A=A[:i-1]+A[i-1]*(Chislo)+A[i:]
            i += Chislo-1    
    i+=1                        
print(A)
