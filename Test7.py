N = 4
Mult = 1
for i in range(2,N+1):
    X = 1
    for j in range(i):
        X *= (N-j)
        print('X=', X)
    print(X)
