#!/usr/bin/python
#coding=utf-8
print "\n### Ficheros ###\n"

### En python un fichero es un objeto del tipo file
## y se crea mediante la función open de dicha clase 

## Los ficheros tienen varios modos de lectura y escritura:
###‘r’: read, lectura. Abre un fichero "existente" en modo lectura
###‘w’: write, escritura. Abre un fichero en modo escritura, 
## si no existe lo crea y si existe lo sobreescribe
###‘a’: append, añadir. Abre un fichero en modo escritura,
## si no existe lo crea y si existe añade el contenido al final
###‘b’: binary, este parámetro indica contenido binario
###‘+’: permite lectura y escritura simultáneas

## Abrir un fichero
f = open("archivo.txt", 'w')

## En los ficheros sólo se puede escribir texto. Se puede
## utilitzar la función write
f.write("Hola que tal")

## Después de escribir cerramos el fichero
f.close()

## Ahora podemos leer el contenido
f = open("archivo.txt", 'r')
print f.read()
f.close()

## O añadir más texto
f = open("archivo.txt", 'a')
f.write("\nNueva línea\nOtra línea")
f.close()

## Ahora con la función readline podemos leer línea a línea
f = open("archivo.txt", 'r')
while True:
      linea = f.readline()
      if not linea: break
      print linea
f.close()
## Podemos utilitzar la función tell() para saber la 
## posición del puntero en todo momento, esta posición 
## corresponde al byte en que estamos
f = open("archivo.txt", 'r')
while True:
      print f.tell()
      linea = f.readline()
      if not linea: break
      print linea
f.close()
## Con la función seek() podemos situar el puntero en un byte
f = open("archivo.txt", 'r')
## Situándonos en el byte 14 leeremos la segunda línea
f.seek(14)
print f.readline()  
f.close()

### Teniendo en cuenta que podemos escribir ficheros en modo 
## binario podemos guardar objetos en un fichero, luego jugando
## con las posiciones y tamaños de esos objetos podemos leerlos
## Pero es más rápido utilizar las funciones de serialización de objetos

class Coordenada():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def escribir(self):
        print "Coordenada en X: %d - Y: %d" % (self.x,self.y)
        
c1 = Coordenada(1,2)
c1.escribir()

c2 = Coordenada(4,3)
c2.escribir()

## Para escribir las coordenadas en un fichero
## usamos la función pickle.dump(objeto, fichero)
import pickle

f = open("coordenadas.bin", 'ab')
pickle.dump(c1, f)
pickle.dump(c2, f)
f.close()

## Para leerlas usaremos pickle.load(fichero)
f = open("coordenadas.bin", 'rb')
cd1 = pickle.load(f)
cd1.escribir()
cd2 = pickle.load(f)
cd2.escribir()
f.close()

## Finalmente podemos borrar los ficheros con
## el método remove de la librería os
import os
os.remove('archivo.txt')
os.remove('coordenadas.bin')


