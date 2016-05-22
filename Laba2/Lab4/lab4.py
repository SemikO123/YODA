def f(x):
    y = np.sin(x)
    #y = 999*(x + 3 + 2.4e-6)
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
        a,b,H,Eps,Iter_Max = 1,25,2,1e-2,20

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
    y = f(x)
    plt.plot(x,y)
    plt.grid(True)
    minY = min(y)
    maxY = max(y)
    plt.axis([a-(b-a)*0.05,b+(b-a)*0.05,
              minY-(maxY-minY)*0.05,maxY+(maxY-minY)*0.05])
    if abs(a-b)/step < 20:
        plt.xticks(np.arange(a,b+1e-9,step))
    for i in X:
        plt.scatter(i,f(i))
    plt.show()

#Вычисление корня методом Брента
def rootf_brent(f,a,b,Eps = 1e-10,maxIter = 100):
    x = optimize.brentq(f,a,b,xtol = Eps, maxiter = maxIter)
    return x

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from math import *

#BEGIN
myLittleInput(manual_input = False)

X = []
A = []
i = a
while (abs(i-b) > 1e-6) and (i < b):
    if i+H > b:
        R = b
    else:
        R = i+H

    
    if f(i)*f(R) < 0:
        X.append(rootf_brent(f,i,R))
        A.append(i)
    elif f(i) == 0:
        X.append(i)
        A.append(i)
    i+=H
if f(b) == 0 :
    X.append(b)
    A.append(b-H)

    
Iter = [0]*len(X)
Errors = [0]*len(X)
printTab(X,A,b,H,Iter,Errors)
Graf(X,a,b,H)
    
    
