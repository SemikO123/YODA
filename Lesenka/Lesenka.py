# Терминология:
# Фундамент - нижний слой кубиков
N = int(input('Введите кол-во кубиков : '))
# Num_From - Список с ко-вами лесенок для
Num_From = [0]
Max_From = [0]
IncArr = [0]

# Max - максимально возможное количество кубиков над фундаментом
Max = 0
Inc = 0
while Max < N:
    Inc += 1
    Max += Inc
    Max_From += [ x - Inc for x in range(Max-Inc+1,Max+1)]
    IncArr += [Inc for i in range(Max-Inc+1,Max+1)]
Max = N - Inc

print('{:^18}|{:^18}|{:^18}|'.format('Number :', 'Max For Number:', 'Inc :'))
print('-'*57)
for i in range(len(Max_From)):
    print('{:^18d}|{:^18d}|{:^18d}|'.format(i, Max_From[i], IncArr[i]))
    print('-'*57)
print('Максимальное кол-во над фундаментом = %d' %Max)
print()
    

Num = 1
for i in range(1,Max+1):
    Num_From.append(1)
    for j in range(1,Max_From[i]+1):
        Num_From[i] += Num_From[j]
        if j == Max_From[i] and i >= 6:
            Num_From[i] -= 1
    Num += Num_From[i]


print('{:^18}|{:^18}|'.format('Number :', 'Num From Number:'))
print('-'*38)
for i in range(len(Num_From)):
    print('{:^18d}|{:^18d}|'.format(i, Num_From[i]))
    print('-'*38)
print('Количество лесенок = %d' %Num)
print()





    
