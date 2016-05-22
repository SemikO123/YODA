# return String from file and 3fields from String
def read1(file):
    Str = file.readline()[:-1]
    if len(Str) == 0:
        return 'ERROR'
    fields = Str.split()
    SN, CR, TI = fields[0].lower(), ' '.join(fields[1:len(fields)-2]).lower(),\
                 fields[len(fields)-2]
    return Str, SN, CR, TI

def gtg878(fields, Params):
    result = True
    for i in range(len(Params)):
        if fields[Params[i][0]-1] != Params[i][1].lower():
            result = False
    return result

#DB_Name = input('Введите имя файла содержащего базу данных : ')
DB_Name = 'data1.txt'
infile = open(DB_Name,'r')

while True:
    N=int(input('Введите кол-во полей(1,2,3)\
по которым будет осуществлен отбор : '))
    if 0<N<4: break
    print('Введенное число должно находится в интервале от 1 до 3')
print()

Param = [[0,' '] for i in range(N)]
print('Поля :\n1.Фамилия\n2.Уголовное преступление\n3.Срок(в годах)\n')
for i in range(N):
    Param[i][0] = int(input('Выберите номер(1-3) %d-го параметра : '%(i+1)))
    Param[i][1] = input('Введите параметр : ')
print()
print('Записи соответствующие критериям :')

CurrLine = read1(infile)
if CurrLine != 'ERROR':
    outfile = open('Out.txt','w')
    while not CurrLine == 'ERROR':
        if gtg878(CurrLine[1:4],Param):
            print(CurrLine[0])
            outfile.write(CurrLine[0]+'\n')
        CurrLine = read1(infile)

infile.close()
outfile.close()







