N = input('Введите строку : ')
NOS = len(''.join(N.split())) #NOS - Number Of Symbols
N = ( ' '*((80-NOS)//(len(N.split())-1)) ).join(N.split())
N = N.replace( ' '*((80-NOS)//(len(N.split())-1)) \
    , ' '*((80-NOS)//(len(N.split())-1)+1),(80-NOS)%(len(N.split())-1))
print(N)
print('Len = ', len(N))
