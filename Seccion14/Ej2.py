
selec = int(input("Ingrese un numero entero positivo: "))

def factorial(ent):
    i = ent - 1
    fact = ent
    while i > 0:
        fact*=i
        i-=1
    print("El factorial de {} es {} ".format(ent,fact))


factorial(selec)