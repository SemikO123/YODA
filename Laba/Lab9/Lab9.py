Text =  ['Python - Высокоуровневый язык язык программирования общего назначения,',
     'ориетированный на повышение производительности язык разработчика и',
     'читаемости язык кода. В то же время стандартная бибилитотека включает',
     'большой объем полезных функций. Python поддерживает несколько парадигм',
     'программирования, в том числе структурное программирование, объектно',
     'ориентированное программирование,  функциональное программирование,',
     'императивное и АОП. Основные архитектурные черты - динамическая',
     'типизация, автоматическое управление памятью, полная интроспекция,',
     'механизм обработки исключений.']
print('Текст :')
for i in Text:
    print(i)
print()

# Создаем массив из предложений текста 
Text2 = ''.join([x+' ' for x in Text]).split('.')
del(Text2[len(Text2)-1])
for i in range(len(Text2)):
    Text2[i] = Text2[i].strip()

S = [i.lower() for i in Text2]
    
for i in S:
    print(i)
print()

# Избавляемся от знаков препинания
for i in range(len(S)):
    j = 0
    while j < len(S[i]):
        if ('z'<S[i][j] or S[i][j]<'a') and ('я'<S[i][j] or S[i][j]<'а')\
                                          and S[i][j] !=' ':
            S[i] = S[i][:j] + S[i][j+1:]
        else:
            j +=1
            
for i in S:
    print(i)
print()

for i in range(len(S)):
    S[i] = S[i].split()
for i in S:
    print(i)

MaxNum = 0;
IndMax = -1;
for i in range(len(S)):
    MaxCurr = 0
    for Word in S[i]:
        if S[i].count(Word) > MaxCurr:
            MaxCurr = S[i].count(Word)
    if MaxCurr > MaxNum:
        MaxNum, IndMax = MaxCurr, i
print()
if IndMax != -1:
    print(Text2[IndMax])
    #print('Максимальное количество слов = %d'%MaxNum)




 



    

