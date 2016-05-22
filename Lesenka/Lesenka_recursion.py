# Терминология:
# Фундамент - нижний слой кубиков
N = int(input('Введите кол-во кубиков : '))
# Num_From - Список с ко-вами лесенок для
Num_From = [0]
Max_For = [0]

# Max - максимально возможное количество кубиков над фундаментом
Max = 0
Inc = 0
while Max < N:
    Inc += 1
    Max += Inc
    Max_For += [ x - Inc for x in range(Max-Inc+1,Max+1) ]
Max = N- Inc
Max_For[0] = Max

print('{:^18}|{:^18}|'.format('Number :', 'Max For Number:'))
print('-'*38)
for i in range(len(Max_For)):
    print('{:^18d}|{:^18d}|'.format(i, Max_For[i]))
    print('-'*38)
print('Максимальное кол-во над фундаментом = %d' %Max)
print()

Num = 1
deep = 1
Ind = [N,1]
while Ind[deep] <= Max_For[Ind[deep-1]] or deep > 1:
    print(' '*(deep-1)*3, 'deep = %d  Ind[%d] = %d' %(deep,
                                                  deep, Ind[deep]), sep='')
    if Ind[deep] > Max_For[Ind[deep-1]]:
        del(Ind[deep])
        Ind[deep-1]+=1
        deep-=1
        print(' '*(deep-1)*3,'DEL MAFAKA Deep = %d' %deep, sep='')
        continue
    if Ind[deep] <= 2:
        if Ind[deep-1]-Ind[deep] > Ind[deep]:
            Num+=1
            print(' '*(deep-1)*3,'INCREASE SLUCHAETSYA', sep='')
    else:
        if  Ind[deep-1]-Ind[deep]>Ind[deep]:
            Num+=1
            print(' '*(deep-1)*3,'INCREASE SLUCHAETSYA', sep='')
        Ind.append(1)
        deep+=1
        continue
    Ind[deep]+=1
print('Количество лесенок = %d' %Num) 
            
'''print('{:^18}|{:^18}|'.format('Number :', 'Num From Number:'))
print('-'*38)
for i in range(len(Num_From)):
    print('{:^18d}|{:^18d}|'.format(i, Num_From[i]))
    print('-'*38)
print('Количество лесенок = %d' %Num)
print()'''





    
