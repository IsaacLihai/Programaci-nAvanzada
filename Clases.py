#Una clase tiene propiedades, caracteristicas o atributos
#Además de las funcionalidades

#Los nombres de las clases empiezan por mayuscula
class Persona():
    #Propiedades, caracteristicas o atributos:
    apellidos =""
    nombres = ""
    edad = 0
    despierta = False

    #Funcionalidades

    def despertar(self):
        self.despierta = True
        print("Bienvenido")

#crear objetos

persona1 = Persona()
persona1.apellidos = "Akerman"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)