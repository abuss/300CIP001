import random

x = [5,4,6,2,8,4,7,2,1,9,3]
y = list(range(10,0,-1))
# y = list(range(20))

def quicksort(l):
    print(l)
    if len(l)<2:
        return l
    pivote = l[0]
    menores = [x for x in l[1:] if x < pivote]
    mayores = [x for x in l[1:] if x >=  pivote]

    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(y))
print("-"*20)
print(quicksort(x))

print("="*25)
def quicksort2(l):
    print(l)
    if len(l)<2:
        return l
    pivote = l[random.randrange(len(l))]
    l.remove(pivote)
    menores = [x for x in l if x < pivote]
    mayores = [x for x in l if x >=  pivote]

    return quicksort2(menores) + [pivote] + quicksort2(mayores)

print(quicksort2(y))
print("-"*20)
print(quicksort2(x))
