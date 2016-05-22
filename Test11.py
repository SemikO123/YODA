import math as m
mult = 1
k = 16
for i in range(16):
    mult *= k
    k-=1

print(mult)

st = m.log2(mult)
print(st)
