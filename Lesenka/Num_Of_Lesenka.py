def num(N):
    MIn = 0
    Inc = 0
    while MIn < N:
        Inc += 1
        MIn += Inc
        Min_For += [ Inc for x in range(MIn-Inc+1,MIn+1) ]
    
    Num = 1
    deep = 1
    Ind = [N,Min_For[N]]
    Sum = 0
    while Ind[deep] <= Ind[deep-1]-1 or deep > 1:
        # Если кол-во кубиков на уровне становится равно предыдущему,
        # то подняться на уровень
        if Ind[deep] == Ind[deep-1]:
            del(Ind[deep])
            deep -= 1
            Sum -= Ind[deep]
            Ind[deep] += 1
            continue
        
        Sum += Ind[deep]
        # Если Sum становится равен кол-ву кубов, то подняться на уровень
        if Sum == N:
            Num += 1
            if Out_Flag:
                for i in range(1,deep+1):
                    print(Ind[i], end='  ')
                print()
                      
            Sum -= Ind[deep]
            del(Ind[deep])
            deep -= 1
        # Если текущий кол-во больше 2 -> можно поставить еще этаж ->
        # -> опуститься на уровень 
        elif Ind[deep]>=2:
            # N-Sum - Min_For[N-Sum] - минимальное кол-во кубиков в фундаменте
            # лестницы которую требуется образовать на следующем этаже
            Ind.append(Min_For[N-Sum])
            deep += 1
            continue
        # Из суммы вычитается текущее кол-во кубиков на уровне,
        # а само кол-во увеличивается
        Sum -= Ind[deep]
        Ind[deep] += 1
    return N
    
