class Calculadora():

    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2
    
    def sumar(self):
        print("La suma es: ",self.int1 + self.int2)

    def restar(self):
        print("La resta es: ",self.int1 - self.int2)

    def multiplicar(self):
        print("La multiplicacion es: ",self.int1 * self.int2)

    def dividir(self):
        print("La division es: ",self.int1 / self.int2)



numero = Calculadora(10 , 2)

numero.sumar()
numero.restar()
numero.multiplicar()
numero.dividir()