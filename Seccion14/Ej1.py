from select import select


lista = []
listaimp = []
listapar = []

def lista1():
    i = 0
    while i <= 5:
        selec = int(input("Ingrese un numero a la lista: "))
        lista.append(selec)
        i+=1

def ordenar():
    i=0
    while i <= 5:
        if (lista[i] % 2) == 0:
            listapar.append(lista[i])
        else:
            listaimp.append(lista[i])
        i+=1
    print("La lista impar es",listaimp)
    print("La lista par es ",listapar)


lista1()

ordenar()