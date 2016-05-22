N=int(input())
if N<2:print('Нельзя')
i=2;G=N
while i<=N and N>1:
    if i==G:print('Простое');break
    if N%i:i+=1
    else:print(i);N//=i
