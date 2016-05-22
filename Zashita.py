from math import *
x1, y1 = map(float, input('Введите координаты 1-ой вершины : ').split())
x2, y2 = map(float, input('Введите координаты 2-ой вершины : ').split())
x3, y3 = map(float, input('Введите координаты 3-ой вершины : ').split())
x4, y4 = map(float, input('Введите координаты точки M : ').split())

Dist1 = abs((x4-x1) * (y2-y1) - (y4-y1) * (x2-x1)) / sqrt((x2-x1)**2 + (y2-y1)**2)
Dist2 = abs((x4-x2) * (y3-y2) - (y4-y2) * (x3-x2)) / sqrt((x3-x2)**2 + (y3-y2)**2)
Dist3 = abs((x4-x3) * (y1-y3) - (y4-y3) * (x1-x3)) / sqrt((x1-x3)**2 + (y1-y3)**2)
print('Расстояние до наиболее удаленной стороны = ', '{:.4f}'.format(max(Dist1, Dist2, Dist3)))
