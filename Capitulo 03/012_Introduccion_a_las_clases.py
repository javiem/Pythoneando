#!/usr/bin/python
#coding=utf-8
print "\n### Programacion Orientada a Objetos: Introducci�n###"

## Definicion de la clase
class Persona:
    
    ## Inicializador
    def __init__(self, nombre, edad):
        ## Asignacion de variables
        self.nombre = nombre
        self.edad = edad
        print "-- Usuario creado --\nNombre:" , nombre, "\nEdad:", edad
        
    ## Metodos de la clase
    def mayor_de_edad(self):
        if self.edad >= 18:
            print self.nombre, "es mayor de edad" 
        else :
            print self.nombre, "es menor de edad"
    def aniversario(self):
        self.edad += 1
        print self.nombre, "cumple y ahora tiene", self.edad
        
## Instanciamos una persona y ejecutamos algunos metodos
    
p = Persona("Hector", 22)
p.mayor_de_edad()
p.aniversario()