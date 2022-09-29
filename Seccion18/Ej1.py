class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre {} : Nota {}".format(self.nombre , self.nota))

    def resultado(self):
        if self.nota < 7:
            print("Reprobado")
        else:
            print("Aprobado")


alumno = Estudiante("Facundo", 9)
alumno.imprimir()
alumno.resultado()


