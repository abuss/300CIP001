__author__ = 'abuss'

def print_fibo(k):
    antepenultimo = 0
    penultimo = 1
    pos = 1
    while pos <= k:
        actual = antepenultimo + penultimo
        print(pos,penultimo)
        antepenultimo = penultimo
        penultimo = actual
        pos = pos +1

print_fibo(10)
