from math import *
x = float(input('Введите X : '))
Eps = float(input('Введите точность Eps : '))
Num = 0
Curr = x
Summ = Curr
# print('Сurrent %f Num %d' %(Curr, Num))
while abs(Curr) > Eps:
    Num += 1
    Curr = (-1)*Curr*x*x / (2*Num + 1) / (2*Num)
    # print('Сurrent %f Num %d' %(Curr, Num))
    Summ += Curr
print(Summ)
