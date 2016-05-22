X = list(map(int,input('Введите массив X : ').split()))
Y = list(map(int,input('Введите массив Y : ').split()))

Z=[]
k1 = k2 = 0
while k1 < len(X) and k2 < len(Y):
    if X[k1] <= Y[k2]:
        Z.append(X[k1])
        k1 +=1
    else:
        Z.append(Y[k2])
        k2 +=1
if k1 < len(X):
    Z += X[k1:len(X)]
if k2 < len(Y):
    Z += Y[k2:len(Y)]
print(Z)
        
