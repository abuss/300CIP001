def pintar(x):
    for i in x:
        for j in i:
            if j==1:
                print '*',
            else:
                print " ",
        print

def pintar2(x):
    i = 0
    while i<len(x):
        j = 0
        while j < len(x[i]):
            if x[i][j]==1:
                print '*',
            else:
                print " ",
            j+=1
        print
        i+=1

x = [[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]]
c = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]

pintar(x)
print
pintar(c)
