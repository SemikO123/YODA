''' Вычисление интеграла методом срединных прямоугольников и методом 3/8'''
from math import *

def PrintIn(I):
    if I =='ERROR':
        return 'Интегрирование невозможно'
    else:
        if I< 1e-05 or I > 1e+05:
            return '{:.6e}'.format(I)
        else:
            return '{:.8f}'.format(I)

# Функция
def Function(x):
    return x+1

def Mid(L, R, Num):
    H = abs((L-R) / Num)
    Summ = 0;
    for i in range(Num):
        L += H
        Summ += Function(L-(H/2));
    return Summ*H

def M38(L, R, Num):
    if Num %3 != 0:
        return('ERROR')
    else:
        h = abs(R-L)/Num
        summ = 0
        while abs(R-L) >= h*3-(1e-07):
            summ +=Function(L)+ 3*Function(L+h) + 3*Function(L+2*h) + Function(L+3*h)
            L += 3*h
        return summ * h*3/8
            

a,b = map(int, input('Через пробел введите \
левую и правую границу отрезка : ').split())        
n1, n2 = map(int, input('Через пробел \
введите n1, n2- количества разбиений отрезка : ').split())
Eps = float(input('Введите точность для вычисления интеграла : '))
print()

# Вывод таблицы
print('{:<25}|{:^25}|{:^25}'.format('Метод:', 'n1=%d'%n1, 'n2=%d'%n2))
print('-'*73)
print('{:<25}|{:^25}|{:^25}'.format('Срединных прямоугольников',
                                    PrintIn(Mid(a,b,n1)),PrintIn(Mid(a,b,n2))))
print('{:<25}|{:^25}|{:^25}'.format('Метод 3/8',
                                    PrintIn(M38(a,b,n1)),PrintIn(M38(a,b,n2))))

print('\nМетод с наименьшей точностью - Срединные прямоугольники')
N = 1
while abs(Mid(a,b,N) - Mid(a,b,2*N)) > Eps:
    N*=2
print('Значение интеграла с заданой точностью = ',PrintIn(Mid(a,b,N)))
print('Количество разбиений для вычисления = %d'%N)



