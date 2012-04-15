#!/usr/bin/python
#coding=utf-8
print "\n### Excepciones ###\n"

## Lista completa con todos los tipos de excepciones que puede lanzar Python
## http://docs.python.org/library/exceptions.html

## Lanzar una excepción

def dividir(a,b):
    return a/b

# ZeroDivisionError: integer division or modulo by zero
# dividir(5,0)

# Capturar y tratar excepciones
# Abrir un fichero que no existe
try:
    f = file("archivo.txt")
except:
    print "El archivo no existe"

## Tratar varias excepciones por bloque
try:
    # Parsear un entero incorrecto
    num = int("3a")
    # Imprimir una variable que no existe
    print no_existe
except NameError:
    print "La variable no existe"
except ValueError:
    print "El valor no es un numero"

## Cláusula con else
## La cláusula finally siempre se ejecuta
try:
    print "Bloque try"
    8 / 0
    print "Try después de error" # Nunca debería llegar aquí
except ZeroDivisionError:
    print "Bloque exception division por cero"
finally: # el bloque finally se ejecuta siempre una vez lanzada cualquiera excepcion
    print "Bloque finally"
    
## Crear nuestras propias excepciones
class MyError(Exception):
    def __init__(self, value): # Necesitan un método init
        self.value = value
    def __str__(self):  # Y un str para devolver el error
        return repr(self.value)

try:
    raise MyError(2*2) # Con raise podemos lanzar la excepción
except MyError as e:
    print 'Excepcion MyError lanzada, valor:', e.value