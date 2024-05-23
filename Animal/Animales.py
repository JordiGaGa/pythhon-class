# Animales 
class animal():
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido

    def haz_ruido(self):
        print(self.sonido)

class perro(animal):
    def juega(self):
        print(f"{dog.nombre} quiere jugar")

class gato(animal):
    def usa_arenero(self):
        print(f"{cat.nombre} se encuentra cagando")


dog = perro("Tobi", 11, "guau" )
print(dog.__dict__)
dog.haz_ruido()
dog.juega()
cat = gato("Fideos", 11, "miau")
cat.haz_ruido()
cat.usa_arenero()

dog.__dict__

    