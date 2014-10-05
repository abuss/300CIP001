def power(a,b):
    "Calcula a elevado a la b"
    res = 1
    cb = 0
    while cb<b:
        res = res * a
        cb+=1
    return res

print power(2,4)
print power(5,3)
 
