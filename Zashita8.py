def F(x):
    return x*x

def PrintInt(I):
    if I<1e-6 or I>1e+4:
        return '{:.5e}'.format(I)
        
    else:
        return '{:.5f}'.format(I) 

def Parab(L,R,Num):
    h = abs(R-L)/Num
    summ = 0
    summ += F(L) + F(R)
    L +=h
    for i in range(2,Num+1):
        if i%2 == 0:
            summ += 4*F(L)
        else:
            summ += 2*F(L)
        L +=h
    return summ*h/3


a,b = map(float,input('Введите верхний и нижний пределы интегрирования : ').split())
Eps = float(input('Введите точность вычисления интеграла : '))



N = 1
while abs(Parab(a,b,N)-Parab(a,b,2*N)) > Eps:
    N *=2
print('Значение интеграла при точности Eps=',Eps,' равно ', PrintInt(Parab(a,b,2*N)), 'кол-во интервалов = ', N*2)
