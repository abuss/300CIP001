def fact(n):
    "Calcula el factorial de n"
    if n==1:
        return 1
    else:
        return fact(n-1)*n

print("2!:",fact(2))
print("5!:",fact(5))
print("13!:",fact(13))
