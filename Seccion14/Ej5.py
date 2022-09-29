import math

def area_cuadrado(base, altura):
    area = base * altura
    return  area

def area_circulo(radio):
    area = math.pi * radio
    return area

print(area_cuadrado(2, 3))

print(area_circulo(3))