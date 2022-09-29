alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

opt = int(input("Ingrese el numero de posicion: "))

if opt <=27 and opt >0:
    print("La letra del abecedario que corresponde con la posicion {} es {}".format(opt,alfabeto[opt-1].upper()))
else:
    print("Esa posicion no tiene una letra asignada en el abecedario")