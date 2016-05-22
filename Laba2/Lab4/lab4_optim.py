def f(x):
    #y = x*x-x-2#np.sin(x)
    #y = 999*(x + 3 + 2.4e-6)
    #y = 999*sin(x)
    #y = abs(sin(x))-0.5
    #y = sin(x)
    y = sin(x)*sin(x*x)
    #y = np.sin(x)/x
    return y
def fi(x):
    y = cos(x)

def fi(f,x,Eps = 1e-8):
    y = (f(x+Eps)-f(x))/Eps
    return round(y,6)

#Ввод данных 
def myLittleInput(manual_input = True):
    if manual_input:
        global a,b,H,Eps,Iter_Max,H2,EpsE
        a,b = map(float, input('Введите левую и правую\
 границы интервала через пробел: ').split())
        H = float(input('Введите шаг: '))
        Eps = float(input('Введите точность вычисления: '))
        Iter_max= int(input('Введите максимальное кол-во итераций: '))
        H2 = float(input('Введите шаг для нахождения экстремумов: '))
        EpsE = float(input('Введите точность вычисления экстремумов: '))
    else:
        a,b,H,Eps,Iter_Max,H2,EpsE = -10,10,0.001,1e-12,50,0.01,1e-6

#Печать таблицы
def printTab(X,A,b,Step,Iter_Num,Errors,):
    print('{:^5}|{:^5}{:^5}|{:^10}|{:^12}|{:^12}|{:^10}'.format(
        'N','A','B','X','f(x)','итерации','ошибка'))
    for i in range(len(X)):
        print('-'*65)
        if A[i]+Step > b:
            R = b
        else:
            R = A[i]+Step        
        print(
        '{:^5d}|{:^5.2g}{:^5.2g}|{:^10.7g}|{:^12.4g}|{:^12d}|{:^10d}'.format(
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

#Вывод графика
def Graf(X,a,b,step,Eps):
    x = np.arange(a,b+0.01,0.001)
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
        if (a<= i <= b) and (abs(f(i)) < Eps*100):
            plt.scatter(i,f(i))
    plt.show()

#Биекция
def biect(f,a,b):
    c = (a+b)/2
    if f(a)*f(c) < 0:
        b = c
    elif f(c)*f(b)<0:
        a = c
    return a,b

#def Extremum(

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
        print(a,c,b)
        x = c
        ErrorCode = 3
        return x, Iter, ErrorCode
    x = b + (P/Q)
    
    if not(a < x < b):
        l,r = biect(f,a,b)
    elif abs(f(x)) < Eps:
        ErrorCode = 0
        return x, Iter, ErrorCode
    elif f(x)*f(a) > 0:
        l,r = x,b
    elif f(x)*f(b) > 0:
        l,r = a,x
    #При недостаточной эфективности схождения применяется биекция
    if  (b-a)/(r-l) < 2 :
        l,r = biect(f,a,b)
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
Graf(X,a,b,H,Eps)
    
    
