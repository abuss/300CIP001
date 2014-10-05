def fact(n):
    "Calcula el factorial del numero n"
    x = 1
    res = 1
    while x<=n:
        res = res * x
        print "x:",x,"res:",res
        # x = x+1
    return res

res = fact(5)
print "5!=",res

