from math import sqrt
a, b, c = map(float, input('ax^2 + bx + c = 0\nВведите коэффициены a, b, c : ').split())
D = b**2 - 4*(a*c)
if a == 0 :
    if b != 0 :
        print('x = ','{:.6f}'.format((-c / b)))
    else :
        if c == 0 :
            print('x - любое чсло')
        else :
            print('введенные данные не верны, мне жаль')
else :
    if D > 0 :
        print('x1 = ','{:.6f}'.format((-b + sqrt(D)) / (2*a)))
        print('x2 = ','{:.6f}'.format((-b - sqrt(D)) / (2*a)))
    elif D == 0 :
        print('x = ','{:.6f}'.format( -b/(2*a)))
    else :
        print('Среди действительных чисел корней нету')
    
    
