def buscar(x,D):
    for r in D:
        if (r[0]<=x and x <=r[1]):
            return True
    return False


d = [[-3,1],[4,8],[10,100]]
print "5 in",d," esta?: %s" % buscar(5,d)
print "2 in",d," esta?: %s" % buscar(2,d)
print "3.999 in",d," esta?: %s" % buscar(3.999,d)
