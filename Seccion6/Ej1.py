a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

resolv1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
resolv2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print('El valor de la resolvente es', resolv1,'y',resolv2)
