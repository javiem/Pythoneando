#!/usr/bin/python
#coding=utf-8
print "\n### Programacion Orientada a Objetos: Encapsulacion ###"

"""La encapsulación se refiere a impedir el acceso a determinados mé-
todos y atributos de los objetos estableciendo así qué puede utilizarse
desde fuera de la clase."""

## Clase con métodos privados y públicos
class Ejemplo:
    def publico(self): # método público
        print "Metodo público" # método privado
    def __privado(self):
        print "método privado" # podemos llamar al método privado des de uno público
    def llamar_privado(self): 
        self.__privado()
        
e = Ejemplo()

# Metodo publico
e.publico()

# Metodo privado da error
# AttributeError: Ejemplo instance has no attribute '__privado'
# e.__privado()

# Llamar un metodo privado a partir de uno público no da error
e.llamar_privado()

# El doble guión indica que se renombra incluyendo el nombre de la clase
# Con un pequeño truco se puede engañar a Python y llamar al método privado
e._Ejemplo__privado()

# Hemos visto como encapsular métodos, ahora veremos como encapsular atributos
# con los métodos get y set, una práctica común en la mayoría de lenguajes
# orientados a objetos. Ambos métodos son públicos y permiten modificar y leer 
# los atributos privados de nuestra clase, lo que nos permite filtrar los valores
# antes de editar los valores

## setNombre_variable: establece el valor
## getNombre_variable: lee  el valor

class Nota:
    def __init__(self):
        self.__nota = 0;
    def getNota(self):
        return self.__nota
    def setNota(self, nota):
        if nota <= 10 and nota >= 0 :
            self.__nota = nota
        else : 
            print "Nota incorrecta"
            
n = Nota()
print n.getNota() 
n.setNota(7)
print n.getNota() 
n.setNota(11)

# Podemos abstraer al usuario de utilizar estos métodos definiendo propiedades
# Creamos una clase de nuevo estilo heredando de la clase base object y asi tendremos
# acceso a funcionalidades avanzadas

class Nota(object):
    def __init__(self):
        self.__nota = 0;
    def getNota(self):
        return self.__nota
    def setNota(self, nota):
        if nota <= 10 and nota >= 0 :
            self.__nota = nota
        else : 
            print "Nota incorrecta"
    nota = property(getNota, setNota)  
           
n = Nota()
print "\n", n.nota
n.nota = 7
print n.nota
n.nota = 11
