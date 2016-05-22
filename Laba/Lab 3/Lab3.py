from math import *
x = float(input('Введите значение параметра X : '))
eps = float(input('Введите значение Eps : '))
N = int(input('Введите номер с которого надо начать вывод : '))
St = int(input('Введите шаг для печати : '))
Max = int(input('Введите максимальную длину последовательности : '))

Num = 0  # Текуций номер элемента последовательности
Sum = 1  # Сумма последовательности
Curr = 1 # Текущий элемент
print('*' * 70)
print('n\t\tCurrent Summ:\t\tCurrent Element:')
print('{}\t\t{:.4e}\t\t {:.5e}'.format(Num, Sum, Curr))
while abs(Curr) > eps :
    if (Num - N) % St == 0 and Num >= N:
        print('{}\t\t{:.4e}\t\t {:.5e}'.format(Num, Sum, Curr))
    Num += 1
    if Num > Max :
        break
    Curr = pow(-1, Num) * (Num+1) * (Num+2) * pow(x, Num) / 2
    Sum += Curr
print('*' * 70)
if Num > Max:
    print('За ', Max, ' шагов воследовательность не сходится')
else :
    print('При x = ', x, ', с точностью Eps = ', eps, ' сумма последовательности = ', '{:.5e}'.format(Sum)) 

