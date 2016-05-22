A = input('Введите строку содержащую слова резделенные пробелами,\n\
слова могут содержать любые символы : ')

# Количество встреч символа с индексом i = Num_Of_Simb[i]
Num_Of_Simb = []
# Топ-5 самых часто встречающихся символов Top_Numb[]
# Num - кол-во букв которое надо найти
Num = 5
Top_Numb = [[' ',0] for i in range(Num)]

for i in range(len(A)):
    if A[i] == ' ':
        Num_Of_Simb.append(0)
    else:
        Curr_Count = A.count(A[i])
        Num_Of_Simb.append(Curr_Count)
        # В заносится в Топ самых частых если больше
        # минимального и еще не находится в нем
        if A.count(A[i]) > Top_Numb[0][1] and\
           not [Top_Numb[j][0] for j in range(len(Top_Numb))].count(A[i]):
            Top_Numb[0] = [A[i], Curr_Count]
            for j in range(len(Top_Numb)-1):
                if Top_Numb[j][1] > Top_Numb[j+1][1]:\
                   Top_Numb[j],Top_Numb[j+1] = Top_Numb[j+1],Top_Numb[j]
#print(Top_Numb)
if Top_Numb[0][1] == 0:
    print('В строке менее %d различных символов'%Num)
else:
    Top_Numb = [Top_Numb[i][0] for i in range(len(Top_Numb))]
    print('\n%d самых часто встречающихся символов : '%Num)
    for i in Top_Numb:
        print(i, end=' ')
    print()
    
    # Перебор всех возможных слов из Num символов
    Words = []
    Ind = [0]
    Curr_ABC = [Top_Numb[:]]
    deep = 0
    while Ind[deep] <= len(Curr_ABC)-1 or deep >= 0:
        
        if Ind[deep] == len(Curr_ABC[deep]):
            if deep == 0:
                deep -= 1
                continue
            del(Curr_ABC[deep])
            del(Ind[deep])
            deep -= 1
            Ind[deep]+=1
            continue
        
        if deep < len(Curr_ABC[0])-1:
            deep +=1
            Curr_ABC.append(Curr_ABC[deep-1][:Ind[deep-1]] + Curr_ABC[deep-1][Ind[deep-1]+1:])
            Ind.append(0)
            continue
        else:
            Curr_Word = ''
            for i in range(len(Curr_ABC[0])):
                Curr_Word += Curr_ABC[i][Ind[i]]
            Words.append(Curr_Word)

            del(Curr_ABC[deep])
            del(Ind[deep])
            deep -= 1
            Ind[deep]+=1
            continue
        
    # Печать таблицы
    i = 0
    print('-'*(Num*5+6))
    while i < len(Words):
        print('|',Words[i], sep='', end='')
        if (i+1)%5 == 0:
            print('|')
            print('-'*(Num*5+6))
        i+=1
    
# Замена символов на кол-во вхождений
A=''
for i in Num_Of_Simb:
    if i < 1:
        A += ' '
    elif i < 10:
        A += str(i)
    else:
         A += ',' + str(i) + ','
print('Строка после замены всех символов на кол-во их вхождений в строку :')
print(A)
print()

# Замена слов на их среднее арифметическое         
A=''
Curr,CurrLen = 0,0
for i in Num_Of_Simb:
    if i > 0:
        Curr +=i
        CurrLen +=1
    elif CurrLen > 0:
        A += str(round(Curr / CurrLen)) + ' '
        Curr,CurrLen = 0,0
    else:
        A += ' '
if CurrLen > 0:
        A += str(round(Curr / CurrLen)) + ' '
print('Строка после замены слов их средним арифметическим :')
print(A)
