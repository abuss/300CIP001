def fibonacci(n):
    "Imprime los primeros n numeros de la serie Fibonacci"
    p_ultimo = 0
    ultimo = 1
    x = 1
    print ultimo,
    while x < n:
        actual = p_ultimo + ultimo
        print ",",actual,
        p_ultimo = ultimo
        ultimo = actual
        x = x+1

fibonacci(9)
