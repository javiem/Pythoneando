#!/usr/bin/python
#coding=utf-8
print "\n### Docstrings ###\n"

## Todos los objetos en Python tienen una variable especial
## llamada __doc__ . Esta variable es más ni menos que una
## cadena y sirve para definir la documentación

## Si el primer estamento declarado en un objeto es una cadena
## ésta se asocia con el docstring. También se puede definir 
## manualmente con nombre_objeto.__doc__ = "Cadena"

## Recordemos que todo en Python son objetos, así que todo
## puede tener una pequeña documentación para ser visualizada
## con el comando de ayuda help

class Figura:
    """Clase para crear una figura en el plano"""
    
    ## Inicializador
    def __init__(self, x, y, color):
        ## Asignacion de variables
        self.x = x
        self.y = y
        self.color = color
        
    def dibujar(self):
        """Método que da la localización de la figura"""
        print "Figura dibujada en coordenadas:\n  X:" , self.x, "\n  Y:", self.y
        print "  Color:", self.color  
        
F = Figura(10, -2, "verde")

help(F)
help(F.dibujar)

def funcion_echo(variable):
    print variable

funcion_echo.__doc__ =  """Método que muestra lo que recibe"""
help(funcion_echo)
funcion_echo("Hola mundo!")