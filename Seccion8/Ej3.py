palabra_1 = input("Ingrese la primer palabra: ")
palabra_2 = input("Ingrese la segunda palabra: ")
if palabra_1[-3:] == palabra_2[-3:]:
    print("Las palabras riman")
else: 
    print("Las palabras no riman")