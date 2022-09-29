class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def car(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def estud(self, name, edad):
        self.name = name
        self.edad = edad
        print("Mi nombre es {} tengo {} años, mi especialidad es {} y estudio en {}".format(self.name,self.edad,self.especialidad,self.nombre))


persona = Estudiante("Universidad Nacional de MDP")
persona.car("Ingenieria en Computacion")
persona.estud("Facundo Fonseca",29)
