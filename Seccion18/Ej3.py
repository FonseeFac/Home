class Fabrica():
    def __init__(self ,llantas ,color ,precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas es ", self.llantas)
        print("El color de la moto es ", self.color)
        print("El precio de la moto es $ ",self.precio)

class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llantas es ", self.llantas)
        print("El color de la carro es ", self.color)
        print("El precio de la carro es $ ",self.precio)


moto = Moto(2,"Rojo",10000)

carro = Carro(4, "Blanco", 20000)

moto.datos()

carro.datos()