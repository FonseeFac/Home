eleccion = input("Ingrese la opcion (A- Partido ROJO , B- Partido VERDE, C- Partido AZUL): ")

if eleccion.upper() == "A":
    print("Usted voto por el Partido ROJO")
elif eleccion.upper() == "B":
    print("Usted voto por el Partido VERDE")
elif eleccion.upper() == "C":
    print("Usted voto por el Partido AZUL")
else:
    print("Usted no selecciono una opcion CORRECTA")