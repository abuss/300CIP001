def primo(n):
    "Retorna True si n es primo False en caso contrario"
    y = 2
    while y <= (n/2):
        if n % y == 0:
            return False
        y = y + 1
    return True



def primeros_n_primos(n):
    "Imprime los primeros n primos"
    i = 0
    x = 2
    while i < n:
        if primo(x):
            print x,
            i = i +1
        x = x + 1

primeros_n_primos(50)
