N = 4
A = [[i*N + j for j in range(N)] for i in range(N)]
for i in A:
    for j in i:
        print(j, end='   ')
    print()

B = [[A[i][j] for j in range(len(A[i]))if i!=j] for i in range(len(A)) ]
print()
for i in B:
    for j in i:
        print(j, end='   ')
    print()
