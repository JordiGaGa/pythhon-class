# Animales 
class animal():
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido

    def haz_ruido(self):
        print(self.sonido)
        
# Eliminamos el "sonido" como atributo y lo dejamos unicamente como método 
class animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def haz_ruido(self):
        print("aaah")

class perro(animal):
    def juega(self):
        print(f"{dog.nombre} quiere jugar")
    # El sonido que emite en animal debe ser un método y no un atributo, de modo que se hace el override 
    def haz_ruido(self):
        print("¡Guau!")

class gato(animal):
    def usa_arenero(self):
        print(f"{cat.nombre} se encuentra cagando")

# Define tu clase gato con su nombre, edad y si usa arenero. 
# En tu caso agredas el usa_arenero como un método cuando en realidad debe ser un atributo 
class gato(animal): 
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad) #Para inicializar los atrbutos heredados
        self.usa_arenero = usa_arenero


dog = perro("Tobi", 11, "guau" )
print(dog.__dict__)
dog.haz_ruido()
dog.juega()
cat = gato("Fideos", 11, "miau")
cat.haz_ruido()
cat.usa_arenero()

dog.__dict__

    
