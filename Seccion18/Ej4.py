class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    def mensaje(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)


foqui = Foca()

foqui.mensaje("Soy una foca")
foqui.hablar()

marino = Marino()
marino.hablar()

pulpi = Pulpo()
pulpi.hablar()