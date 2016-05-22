''' В СТРОКЕ указано число k(3<=k<=38) и k целых чисел.
Определить первый экстремум в последовательности k чисел.
Если экстремумов нет, то вывести соотв. сообщение '''
Str = input('Введите данные : ')
while len(Str.split()) != int(Str.split()[0])+1 :
    Str = input('Введите данные повторно : ' )
k = int(Str.split()[0])
Elem0 = 0
Elem1 = 0
Elem2 = 0
for i in range(1,k+1):
    Elem0 = Elem1
    Elem1 = Elem2
    Elem2 = int(Str.split()[i])
    if i >= 3:
        if (Elem1-Elem0) * abs(Elem2-Elem1) != (Elem2-Elem1) * abs(Elem1-Elem0):
            print('Первый экстремум последовательности = ', Elem1)
            break
else:
    print('Экстремумов нет')
    
