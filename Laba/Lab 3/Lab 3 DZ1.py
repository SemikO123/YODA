from math import *
x = float(input('Введите значение параметра X : '))
eps = float(input('Введите значение Eps : '))
N = int(input('Введите номер с которого надо начать вывод : '))
Max = int(input('Введите максимальную длину последовательности : '))
St = int(input('Введите шаг для печати : '))

Num = 0
Sum = 1
Curr = 1
print('*' * 50)
print('n\t\tCurrent Summ\t\tCurrent Element')
while abs(Curr) > eps :
    if (Num - N) % St == 0 and Num >= N:
        print('{}\t\t{:.4f}\t\t\t  {:2.3e}'.format(Num, Sum, Curr))
    Num += 1
    if Num > Max :
        break
    Curr = pow(-1, Num) * (Num+1) * (Num+2) * pow(x, Num) / 2
    Sum += Curr
print('*' * 50)
if Num > Max:
    print('За ', Max, ' шагов воследовательность не сходится')
else :
    print('При x = ', x, ', с точностью Eps = ', eps, ' сумма последовательности = ', '{:.10f}'.format(Sum)) 

