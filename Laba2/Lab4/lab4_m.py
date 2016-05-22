def f(x):
    #y = np.sin(x)
    #y = 999*(x + 3 + 2.4e-6)
    y = sin(x)
    return y

#Ввод данных 
def myLittleInput(manual_input = True):
    if manual_input:
        global a,b,H,Eps,Iter_Max
        a,b = map(float, input('Введите левую и правую\
 границы интервала через пробел: ').split())
        H = float(input('Введите шаг: '))
        Eps = float(input('Введите точность вычисления: '))
        Iter_max= int(input('Введите максимальное кол-во итераций: '))
    else:
        a,b,H,Eps,Iter_Max = 1,15,2,1e-12,100

#Печать таблицы
def printTab(X,A,b,Step,Iter_Num,Errors,):
    print('{:^5}|{:^5}|{:^5}|{:^10}|{:^12}|{:^12}|{:^10}'.format(
        'N','A','B','X','f(x)','итерации','ошибка'))
    for i in range(len(X)):
        print('-'*65)
        if A[i]+Step > b:
            R = b
        else:
            R = A[i]+Step        
        print(
        '{:^5d}|{:^5.2g}|{:^5.2g}|{:^10.7g}|{:^12.4g}|{:^12d}|{:^10d}'.format(
            i,A[i],R,X[i],f(X[i]),Iter[i],Errors[i]))
    return 0

#Вывод графика
def Graf(X,a,b,step):
    x = np.arange(a,b,0.01)
    y = [f(i) for i in x]
    plt.plot(x,y)
    plt.grid(True)
    minY = min(y)
    maxY = max(y)
    plt.axis([a-(b-a)*0.05,b+(b-a)*0.05,
              minY-(maxY-minY)*0.05,maxY+(maxY-minY)*0.05])
    if abs(a-b)/step < 20:
        plt.xticks(np.arange(a,b+1e-9,step))
    for i in X:
        if (a< i < b) and (f(i) < 1e-4):
            plt.scatter(i,f(i))
    plt.show()

#Биссекция
def bisect(f,a,b):
    c = (a+b)/2
    if f(a)*f(c) < 0:
        b = c
    elif f(c)*f(b)<0:
        a = c
    return a,b

#Вычисление корня методом Брента
def rootf_brent(f,a,b,Eps = 1e-6,maxIter = 100, Iter = 1):
    if Iter > maxIter:
        x = 0
        ErrorCode = 1
        return x, Iter, ErrorCode
    c = (a+b)/2
    
    if f(c) == 0:
        x = c
        ErrorCode = 0
        return x, Iter, ErrorCode
    
    R = f(b)/f(c)
    S = f(b)/f(a)
    T = f(a)/f(c)

    P = S*(T*(R-T)*(c-b)-(1-R)*(b-a))
    Q = (T-1)*(R-1)*(S-1)
    if Q == 0 :
        print(a,'\n',c,'\n',b,sep='')
        print('-'*65)
        ErrorCode = 3
        return 0, Iter, ErrorCode
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

    if  (b-a)/(r-l) < 2 :
        l,r = bisect(f,a,b)
    if abs(f((l+r)/2)) < Eps:
        ErrorCode = 0
        return x, Iter, ErrorCode
    return rootf_brent(f,l,r,Eps,maxIter, Iter+1)

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from math import *

#BEGIN
myLittleInput(manual_input = False)

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
        Iter.append(I)
        Errors.append(Er)
        A.append(i)
    elif f(i) == 0:
        X.append(i)
        Iter.append(0)
        Errors.append(2)
        A.append(i)
    i+=H
if f(b) == 0 :
    X.append(b)
    Iter.append(0)
    Errors.append(2)
    A.append(b-H)

printTab(X,A,b,H,Iter,Errors)
Graf(X,a,b,H)
    
    
