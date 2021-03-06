# Далее следует очевидный фрагмент кода, не нуждающийся в пояснениях
def Circle(x1,y1,x2,y2,x3,y3):
    #Если не выполняется условие x1!=x2 and y1!=y2, то алгоритм не работает
    if x1 == x2 or y1 == y2:
        x2,x3,y2,y3 = x3,x2,y3,y2
    if x1 == x2 or y1 == y2:
        x1,x3,y1,y3 = x3,x1,y3,y1

    # (X-H)^2+(Y-V)^2=R^2
    #H = K*V+C
    K = (-2*y2+2*y1)/(-2*x1+2*x2)
    C = (x2**2 + y2**2 - x1**2 - y1**2)/(-2*x1 + 2*x2)

    V = ( (x3-C)**2 - (x2-C)**2 + y3**2 - y2**2)\
        /( 2*( (x3-C)*K - (x2-C)*K - y2 + y3) )
    H = K*V + C
    
    #sqRadius - квадрат радиуса
    sqRadius = (x1-H)**2+(y1-V)**2
    return H,V,sqRadius

print(Circle(1,2,1,3,2,3))
