def f1(x):
    # y = sin(x) -0.75
    # y = 0.25*x*x*x+2
    # y = x**4-8*x**3+2*x**2-7*x
    y = sin(x)*x
    return y

def fi1(x):
    # y = cos(x)
    #y = 0.75*x*x
    #y = 4*x**3-24*x**2+4*x-7
    y = cos(x)*x+sin(x)
    return y

def fifi1(x):
    #y = -sin(x)
    #y = 1.5*x
    #y = 12*x**2-48*x+4
    y=-sin(x)*x+cos(x)+cos(x)
    return y


def f2(x):
    #y  = cos(x)
    #y = sin(x)*sin(x*x)
    y = (x-2)**2-2
    #y = 2*x/(3*pi)-(2/3)
    return y


def f(x):
    #y = x*x-x-2#np.sin(x)
    #y = 999*(x + 3 + 2.4e-6)
    #y = 999*sin(x)
    #y = abs(sin(x))-0.5
    y = f1(x)-f2(x)
    #y = sin(x)*sin(x*x)
    return y

def Integral(f,a,b,Num_of_part = 1000, Step = 0.001):
    #Step = (b-a)/Num_of_part
    Int = 0
    while (b-a)>(Step*0.1):
        Int += (f(a)+f(a+Step))/2
        a += Step
    Int*=Step
    return Int
    
##def fi(f,x,Eps = 1e-8):
##    y = (f(x+Eps)-f(x))/Eps
##    return round(y,6)

#Ввод данных 
def myLittleInput(manual_input = True):
    if manual_input:
        global a,b,H,Eps,Iter_Max,H2,EpsE
        a,b = map(float, input('Введите левую и правую границы интервала через пробел: ').split())
        H = float(input('Введите шаг: '))
        Eps = float(input('Введите точность вычисления: '))
        Iter_max= int(input('Введите максимальное кол-во итераций: '))
        H2 = float(input('Введите шаг для нахождения экстремумов: '))
        EpsE = float(input('Введите точность вычисления экстремумов: '))
    else:
        a,b,H,Eps,Iter_Max = 0,10,0.1,1e-8,50

#Печать таблицы
def printTab(X,A,b,Step,Iter_Num,Errors,):
    print('{:^5}|{:^6}{:^6}|{:^10}|{:^12}|{:^12}|{:^10}'.format(
        'N','A','B','X','f(x)','итерации','ошибка'))
    for i in range(len(X)):
        print('-'*65)
        if A[i]+Step > b:
            R = b
        else:
            R = A[i]+Step        
        print(
        '{:^5d}|{:^6.3g}{:^6.3g}|{:^10.7g}|{:^12.4g}|{:^12d}|{:^10d}'.format(
            i,A[i],R,X[i],f(X[i]),Iter[i],Errors[i]))
    print()
    frm = '{:^10}|{:^54}'
    print('{:^65}'.format('Таблица ошибок'),'\n','-'*65,sep='')
    print(frm.format('№ ошибки','Описание ошибки:'),'\n','-'*65,sep='')
    print(frm.format('0','Коректная работа'),'\n','-'*65,sep='')
    print(frm.format('1','Превышение кол-ва итераций'),'\n','-'*65,sep='')
    print(frm.format('2','Корень на границе интервала'),'\n','-'*65,sep='')
    print(frm.format('3','Деление на ноль вызванное погрешностью при округлении'),'\n','-'*65,sep='')
    return 0
# clabel
#Вывод графика
def Graf(f1,f2,f,X1,XE,XP,X0,a,b,step,Eps):
    x = np.arange(a,b+0.01,0.001)
    y1 = [f1(i) for i in x]
    y2 = [f2(i) for i in x]
    plt.plot(x,y1, color = 'purple',label = '$f1(x)$')
    plt.plot(x,y2, color = 'red',label ='$f2(x)$')
    x1 = [i for i in x if X0[0]<=i<=X0[len(X0)-1]]
    y12 =[f1(i) for i in x1]
    y22 =[f2(i) for i in x1]
    plt.fill_between(x1,y12,y22,color = 'yellow')
    minY = min(min(y1),min(y2))
    maxY = max(max(y1),max(y2))
    plt.axis([a-(b-a)*0.05,b+(b-a)*0.05,
              minY-(maxY-minY)*0.05,maxY+(maxY-minY)*0.05])
    if abs(a-b)/step < 20:
        plt.xticks(np.arange(a,b+1e-9,step))
    XE = [i for i in XE if a<i<b]
    plt.plot(X1,[f1(i) for i in X1],'co', label = '$Корни$')
    plt.plot(XE,[f1(i) for i in XE],'mo', label = '$Экстремумы$')
    plt.plot(XP,[f1(i) for i in XP],'go', label = '$Перегибы$')
    plt.plot(X0,[f1(i) for i in X0],'bo', label = '$Пересечения$')
##    for i in X1:
##        if (a<= i <= b) and (abs(f1(i)) < Eps*100):
##            plt.scatter(i,f1(i),color = 'cyan')
##    for i in XE:
##        if (a< i < b) and (abs(fi1(i)) < Eps*100):
##            plt.scatter(i,f1(i),color = 'magenta')
##    for i in XP:
##        if (a<= i <= b) and (abs(fifi1(i)) < Eps*100):
##            plt.scatter(i,f1(i),color = 'green')
##    for i in X0:
##        if (a<= i <= b) and (abs(f(i)) < Eps*100):
##            plt.scatter(i,f1(i),color = 'black')
    XE_ext = [a]+XE+[b]
    Min,Max = a,a
    for i in XE_ext:
        if f1(i) < f1(Min):
            Min = i
        if f1(i) > f1(Max):
            Max = i
    plt.scatter(Min,f1(Min),color = 'blue',label='MIN/MAX',linewidth=17)
    plt.scatter(Max,f1(Max),color = 'blue',linewidth=17)
    plt.grid(True)
    plt.legend()
    plt.show()

#Биекция
def bisect(f,a,b):
    c = (a+b)/2
    if f(a)*f(c) < 0:
        b = c
    elif f(c)*f(b)<0:
        a = c
    return a,b



#Вычисление корня методом Брента
def rootf_brent(f,a,b,Eps = 1e-6,maxIter = 100, Iter = 1):
    #Проверка на кол-во итераций
    if Iter > maxIter:
        x = 0
        ErrorCode = 1
        return x, Iter, ErrorCode
    c = (a+b)/2
    
    if abs(f(c)) < Eps:
        x = c
        ErrorCode = 0
        return x, Iter, ErrorCode
    
    R = f(b)/f(c)
    S = f(b)/f(a)
    T = f(a)/f(c)

    P = S*(T*(R-T)*(c-b)-(1-R)*(b-a))
    Q = (T-1)*(R-1)*(S-1)
    if Q == 0 :
        x = c
        ErrorCode = 3
        return x, Iter, ErrorCode
    x = b + (P/Q)
    
    if not(a < x < b):
        l,r = bisect(f,a,b)
    elif abs(f(x)) < Eps:
        ErrorCode = 0
        return x, Iter, ErrorCode
    elif f(x)*f(a) > 0:
        l,r = x,b
    elif f(x)*f(b) > 0:
        l,r = a,x
    #При недостаточной эфективности схождения применяется биекция
    if  (b-a)/(r-l) < 2 :
        l,r = bisect(f,a,b)
    if abs(f((l+r)/2)) < Eps:
        ErrorCode = 0
        return x, Iter, ErrorCode
    return rootf_brent(f,l,r,Eps,maxIter, Iter+1)

def main(f,H,full_output=False):
    X = []
    A = []
    Iter = []
    Errors = []
    i = a
    while (abs(i-b) > 1e-6) and (i < b):
        if i+H > b:
            R = b
        else:
            R = i+H

        
        if f(i)*f(R) < 0:
            x, I, Er = rootf_brent(f,i,R,Eps,Iter_Max)
            X.append(x)
            if full_output :
                Iter.append(I)
                Errors.append(Er)
                A.append(i)
        elif f(i) == 0:
            X.append(i)
            if full_output:
                Iter.append(0)
                Errors.append(2)
                A.append(i)
        i+=H
    if f(b) == 0 :
        X.append(b)
        if full_output:
            Iter.append(0)
            Errors.append(2)
            A.append(b-H)
    if full_output:
        return X,A,Iter,Errors
    else:
        return X
    
# import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from math import *

#BEGIN
myLittleInput(manual_input = False)

X1,A,Iter,Errors = main(f1,H,full_output = True)
if len(X1) > 0:
    printTab(X1,A,b,H,Iter,Errors)
    
XE = main(fi1,H = 0.1)

XP = main(fifi1,H = 0.1)

X0 = main(f,1e-2)
S = 0;
for i in range(len(X0)-1):
    S1 = Integral(f1,X0[i],X0[i+1])
    S2 = Integral(f2,X0[i],X0[i+1])
    if S1*S2 < 0:
        S += abs(S1) + abs(S2)
    elif S1*S2 > 0:
        S += abs(S1-S2)
print()
print('Площадь равна = %.6g'%S)
Graf(f1,f2,f,X1,XE,XP,X0,a,b,H,Eps)
    
    
