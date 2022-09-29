dicc = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

entrada = input("Ingrese el nombre de un pais para conocer su capital: ")

if entrada.title() in dicc:
    print("Su capital es: {}".format(dicc[entrada.title()]))
else:
    print("No se encuentra la capital")
