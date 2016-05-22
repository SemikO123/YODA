Text = ['Тимур - молодец, он вовремя сдаёт лабараторную,',
        'а еще он раз в неделю ездит к бабушке в Жуковский.',
        'A вот Леша не молодец.',
        'Это последнее предложение, оно длиннее. Еж ползет. второго',
        'и это хорошо, на мой взгляд']

print('Text:')
for i in Text:
    print(i)
print()

NewText = ''.join([i+' ' for i in Text]).split('.')
del(NewText[len(NewText)-1])
NewText = [i.strip() for i in NewText]
S = NewText[:]

for i in range(len(S)):
    j = 0
    while j < len(S[i]):
        if ('z'<S[i][j] or S[i][j]<'a') and ('я'<S[i][j] or S[i][j]<'а') and\
           ('Z'<S[i][j] or S[i][j]<'A') and ('Я'<S[i][j] or S[i][j]<'А') and\
                                        S[i][j] !=' ':
            S[i] = S[i][:j] + S[i][j+1:]
        else:
            j +=1
    

for i in range(len(S)):
    S[i] =S[i].split()

Ind = 0
Min = len(S[0])
for i in range(len(S)):
    if len(S[i]) < Min:
        Min, Ind = len(S[i]),i
WInd = -1
Max = 0
for i in range(len(S[Ind])):
    if len(S[Ind][i]) > Max:
        Max,WInd = len(S[Ind][i]),i

NewText[Ind] = NewText[Ind].replace(S[Ind][WInd],'',1).strip()

print('Строка после удаления :')
print(NewText[Ind])
