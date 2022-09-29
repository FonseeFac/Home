selec = int(input("Ingrese el numero del que quiere las tablas de multiplicar: "))
i = 1
if selec < 10:
    while i<10:
        print(" {}x{} = {}".format(i, selec, i*selec))
        i+=1
else:
    print("No es un numero del 1 al 9")