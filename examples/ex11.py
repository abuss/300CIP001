def power(a,b):
    "Calcula a elevado a la b usando solo sumas"
    i = 0
    res = 0
    tmp = 1
    while i<b:
        j = 0
        while j<a:
            res +=tmp
            j+=1
        tmp = res;
        res = 0
        i+=1
    return tmp

a,b = 2,3
print "%d^%d=%d" % (a,b,power(a,b))

a,b = 5,4
print "%d^%d=%d" % (a,b,power(a,b))
