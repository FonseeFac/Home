tupla = ("ENERO", "FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE")

opt = int(input("Ingrese el numero de mes= "))
if opt<=12 and opt >=1:
    print("El numero {} coincide con el mes de {}".format(opt,tupla[opt-1]))
else :
    print("No es un mes del año")