#!/usr/bin/python
#coding=utf-8
print "\n### Pydoc ###\n"

## Es un módulo que incluye Python para crear documentación
## desde su versión 2.1. La propia función help forma parte
## de Pydoc

## Con él podemos generar documentación rápido como en Java
## con Javadoc o con phpdoc en el lenguaje PHP 

## Vamos a generar algo de documentación para la clase Persona
## de una forma fácil con docstrings

class Persona:
    """Clase Persona que simula una persona del mundo real"""
    ## Inicializador
    def __init__(self, nombre, edad):
        """Al constructor se le pasa el nombre de la persona y la edad"""
        ## Asignacion de variables
        self.nombre = nombre
        self.edad = edad
        print "-- Usuario creado --\nNombre:" , nombre, "\nEdad:", edad
        
    ## Metodos de la clase
    def mayor_de_edad(self):
        """Este método sirve para saber si la persona es mayor de edad""" 
        if self.edad >= 18:
            print self.nombre, "es mayor de edad" 
        else :
            print self.nombre, "es menor de edad"
    def aniversario(self):
        """Este método suma 1 a la edad de la persona""" 
        self.edad += 1
        print self.nombre, "cumple y ahora tiene", self.edad
        
## Ahora podemos ejecutar 
## En windows con pydoc en el PATH: > pydoc .\035_Pydoc.py
## En Linux > pydoc ./035_Pydoc.py

## O si queremos generar documentación en html que se guardará en el 
## mismo directorio: > pydoc.py -w pydoc .\035_Pydoc.py

## Incluso podemos poner el server en marcha: > pydoc.py -p 8888
## y entrar desde el navegador http://localhost:8888 para
## ver toda la documentación generada con Pydoc

## Existen proyectos de documentación más avanzados como Docutils,
## Epydoc o Sphinx pero requieren el uso de sintaxis especiales.