from math import *
x1, y1 = map(float, input('Введите координаты 1-ой вершины : ').split())
x2, y2 = map(float, input('Введите координаты 2-ой вершины : ').split())
x3, y3 = map(float, input('Введите координаты 3-ой вершины : ').split())

a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = sqrt((x1 - x3)**2 + (y1 - y3)**2)
if (x2 - x1) * y3 - (y2 - y1) * x3 - (x2 - x1) * y1 + (y2 - y1) * x1 != 0 :
    print('Стороны треугольника =' , '{:.4f} {:.4f} {:.4f}'.format(a, b, c))

    p = (a + b + c) / 2
    h = 2 * sqrt(p * (p - a) * (p - b) * (p - c))
    if a >= b :
        if a >= c :
            h /= a
        else : 
            h /= c
    else :
        if b >= c :
            h /= b
        else :
            h /= c
    print('Высота проведенная из большего угла равна : ' , '{:.4f}'.format(h))

    x4, y4 = map(float, input('Введите координаты точки M :').split())
    dx = x2 - x1
    dy = y2 - y1
    Dist1 = abs(dx * x4 - dy * y4 - y1 * dx + x1 * dy) / sqrt(dx**2 + dy**2)
    if y4 * dx - x4 * dy - y1 * dx + x1 * dy > 0 :
        pm = 1
    elif y4 * dx - x4 * dy - y1 * dx + x1 * dy <0 :
        pm = -1
    else :
        pm = 0
    if y3 * dx - x3 * dy - y1 * dx + x1 * dy > 0 :
        pCh = 1
    else :
        pCh = -1
    if pm == pCh :
        Pos1 = 1
    elif pm == 0 :
        Pos1 = 0
    else :
        Pos1 = -1
        
    dx = x3 - x2
    dy = y3 - y2
    Dist2 = abs(dx * x4 - dy * y4 - y2 * dx + x2 * dy) / sqrt(dx**2 + dy**2)
    if y4 * dx - x4 * dy - y2 * dx + x2 * dy > 0 :
        pm = 1
    elif y4 * dx - x4 * dy - y2 * dx + x2 * dy <0 :
        pm = -1
    else :
        pm = 0
    if y1 * dx - x1 * dy - y2 * dx + x2 * dy > 0 :
        pCh = 1
    else :
        pCh = -1
    if pm == pCh :
        Pos2 = 1
    elif pm == 0 :
        Pos2 = 0
    else :
        Pos2 = -1
        
    dx = x1 - x3
    dy = y1 - y3
    Dist3 = abs(dx * x4 - dy * y4 - y3 * dx + x3 * dy) / sqrt(dx**2 + dy**2)
    if y4 * dx - x4 * dy - y3 * dx + x3 * dy > 0 :
        pm = 1
    elif y4 * dx - x4 * dy - y3 * dx + x3 * dy <0 :
        pm = -1
    else :
        pm = 0
    if y2 * dx - x2 * dy - y3 * dx + x3 * dy > 0 :
        pCh = 1
    else :
        pCh = -1
    if pm == 0 :
        Pos3 = 0
    elif pm == pCh:
        Pos3 = 1
    else :
        Pos3 = -1 
    if Pos1 and Pos2 and Pos3 :
        if Pos1 == Pos2 == Pos3 == 1:
            print('Точка M находится внутри треугольника')
            print('Расстояние до наиболее удаленной стороны =' , max(Dist1, Dist2, Dist3))
        else :
            print('Точка M находится вне треугольника')
    elif Pos1 + Pos2 + Pos3 == 2 or 1 :
        print('Точка M лежит на стороне треугольника')
    else :
        print('Точка M находится вне треугольника')
else :
    print('Точки лежат на одной прямой и не могут образовывать треугольник,  мне жаль')



        
