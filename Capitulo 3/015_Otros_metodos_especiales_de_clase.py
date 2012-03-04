#!/usr/bin/python
#coding=utf-8
print "\n### Programacion Orientada a Objetos: Metodos especiales ###"

## Clase de ejemplo con varios métodos especiales

class Ejemplo(object):
    # Método de inicializacion (NO constructor)
    def __init__(self, atr1, atr2):
        self.atr1 = atr1
        self.atr2 = atr2
        print "Init"
        
    # Método constructor de clase de nuevo estilo,
    # tiene prioridad ante Init
    
    """ def __new__(cls, atr1, atr2):
           print "New" """
        
    # Método destructor con tareas de limpieza
    # Se ejecuta automáticamente al finalizar el programa y libera memoria
    def __del__(self):
        print "Del"
        
    # Método string que devuelve una cadena representado el objeto
    def __str__(self):
        return "arg1=" + str(self.atr1) + " arg2=" + str(self.atr2)
    
    # Método length que devuelve la longitud del objeto en número entero
    def __len__(self):
        return self.atr1 + self.atr2
    
    # Método que implementa comparativas de un objeto == != < > >= <=
    # Debe devolver negativo si nuestro objeto es menor, cero si son iguales y
    # positivo si es mayor
    
    def __cmp__(self, other):    
        #compara las longitudes 
        if len(self) > len(other) : return 1
        elif len(self) < len(other) : return -1
        else : return 0
        
e = Ejemplo(3,5)
print e
print len(e)
f = Ejemplo(3,8)
## ¿Son del mismo tipo?
print e == f
print e < f

