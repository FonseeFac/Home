dicc = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

selecc = int(input("Ingrese el numero de camiseta de un jugador: "))

if selecc in dicc:
    print("El jugador con esa camiseta es: {}".format(dicc[selecc]))
else:
    print("No hay ningun jugador con ese numero de camiseta")