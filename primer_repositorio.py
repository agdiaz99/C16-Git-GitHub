# Consigna: Crear el primer repositorio en GitHub con el material del proyecto de la clase anterior:
# Primer Módulo y Feliz Cumplaños. 

# PRIMER MÓDULO
# 1) Crear un módulo que tenga una clase con atributos y métodos. Instanciar a la clase llamando al módulo desde otro archivo .py
#    Hacer una clase fácil, como Persona, con nombre y apellido, con un método hablar()
#    Crear una instancia de persona, mostrando sus datos y llamando al método desde otro módulo.

class Person():
    def __init__ (self, name, surname, age, gender):
        self.nombre = name
        self.apellido = surname
        self.edad = age
        self.genero = gender
        
    def __str__(self):
        return (f"Hello, my name is {self.nombre} {self.apellido}, I'm {self.edad} years old and I'm a {self.genero}")
    
    def speak(self):
        print("This person is talking")

person_1 = Person("Agustin", "Diaz", 22, "male")
print(person_1)
print(person_1.speak())

# Calcular tu fecha  de cumpleaños lo más preciso posible con datetime y timedelta

from datetime import datetime, timedelta

dt = datetime.now()
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

t = timedelta(days = 60, hours = 6, seconds = 2700)

dia_de_mi_cumpleanos = dt + t
print(dia_de_mi_cumpleanos)