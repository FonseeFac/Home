selec1 = int(input("Ingrese el primer numero: "))
selec2 = int(input("Ingrese el segundo numero: "))

for i in range(selec1,selec2):
    if (i % 2) != 0:
        print(i)
    else:
        continue