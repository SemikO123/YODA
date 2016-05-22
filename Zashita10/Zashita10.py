infile = open('f1.txt','r')
outfile = open('f2.txt','w')

Line = infile.readline()
infile.close()
Ind = 0

while len(Line)!= 0:
    Flag= True
    infile = open('f1.txt','r')
    for i in range(Ind):
        
        Currline = infile.readline()
        if Line == Currline:
            Flag = False
    if Flag:
        outfile.write(Line)
        print(Line[:-1])
    infile.readline()
    Line = infile.readline()
    Ind +=1
    infile.close()   
outfile.close()
