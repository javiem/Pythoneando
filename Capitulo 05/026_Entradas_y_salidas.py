#!/usr/bin/python
#coding=utf-8
print "\n### Entradas y salidas ###\n"

###  ENTRADAS  ###

### Una entrada es una forma de capturar información
## des de el exterior de la aplicación. Por ejemplo
## a través del teclado

### Para capturar un texto por teclado podemos utilizar 
## la función raw_input. Se escribe el texto y se presiona enter
texto = raw_input("Escribe un texto:\n>")
print "El texto escrito es: " + texto

### Si queremos capturar un número tendremos que capturar
## una excepción ValueError para asegurarnos que es correcto
## después de intentar hacer la conversión de texto a entero

try:
    numero = raw_input("Escribe un número entero:\n>") 
    entero = int(numero)
    print "El número introducido es: " + str(entero)
except ValueError:
    print "No has introducido un número y falló la conversión"
    
### También se pueden capturar parámetros des de la línea de comandos
## Es decir ejecutando python fichero.py argumento1 ... argumentoN
## para ello hay que importar la librería sys

### Si compilamos este mismo fichero de la siguiente forma
## python 026_Entradas_y_salidas.py "hola" 4
## Se devolverá:
## > El argumento 0 es 026_Entradas_y_salidas.py
## > El argumento 1 es hola
## > El argumento 2 es 4

import sys

if(len(sys.argv) > 1):
    counter = 0
    for arg in sys.argv:
        print "El argumento " + str(counter) +" es " + sys.argv[counter]
        counter = counter + 1
else:
    print "No hay argumentos"

###  SALIDAS  ###

### La salida por excelencia es la función print() para mostrar texto
## Esta función sólo puede devolver cadenas de texto así que ha que
## transformar todos los tipos a string con la función str()

## Acepta caràcteres de tabulación \t, nueva línea \n y cadenas de 
## varias líneas con triple comilla  """  """

print "Hola\n"
numero = 3
print str(numero)
print """    
    TEXTO
        EN VARIAS
    LÍNEAS """

## Además se pueden concatenar varios tipos diferentes utilizando la suma
print "Hola" + " que tal"

### También son útiles las técnicas de formateo avanzadas
## %s  Cadena
## %d  Entero
## %o  Octal
## %x  Hexadecimal
## %f  Real

entero = 4
cadena = "es entero y el"
real = 3.43

print "El número %d %s %f es real" % (entero, cadena, real)

