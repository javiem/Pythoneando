#!/usr/bin/python
#coding=utf-8
print "\n### Serialización de objetos ###\n"

## En el capítulo 5 vi como trabajar con ficheros, 
## guardar texto y leerlo

## Ahora vamos aun poco más allá viendo como guardar colecciones
## de objetos en un fichero para poderlas reutilizar más adelante 
## Todo ésto se hace con las librerías de serialización de objetos. 

try:
    import cPickle as pickle # Utilizaremos la librería cPickle
except ImportError:          # una implementación de Pickle más
    import pickle            # segura y rápida


""" Guardamos un objeto en un fichero con pickle.dump """

fichero = file("datos.dat", "w") # Cremos un fichero en modo escritura
cosas = ["lampara", "pantalla", "teclado"] # Creamos un objeto lista
pickle.dump(cosas, fichero) # Para guardar el objeto podemos usar el 
                        # método dump de la librería
                        # EL tercer parámetro indicaría el protocolo
                        # de guardado, por defecto es 0 y corresponde
                        # a modo texto, menos eficiente 
fichero.close()

""" Cargamos el objeto del fichero con pickle.load """

fichero = file("datos.dat")
cosas = pickle.load(fichero)
fichero.close()
print cosas

""" Guardamos y cargamos varios objetos en un fichero 
                                     con pickle.dump y pickle.load """

fichero = file("datos.dat", "w")
cosas = ["lampara", "pantalla", "teclado"]
mascosas = ["telefono", "altavoz", "lapiz"]
pickle.dump(cosas, fichero) # Guardamos cada objeto con un dump
pickle.dump(mascosas, fichero)
fichero.close()
fichero = file("datos.dat")
cosas = pickle.load(fichero)    # Luego cada vez que hagamos un load                         
mascosas = pickle.load(fichero) # cargaremos el siguiente objeto
print cosas
print mascosas

## Fácil pero no muy útil. Si tenemos un fichero con miles de objetos
## y queremos cargar el 500 en memoria habría que hacer 500 loads...

## Hay una librería llamada shelve que extiende cPickle y nos permite
## trabajar con objetos y claves de texto asociadas. El método base
## es open y nos generará un diccionario con todos los objetos

""" Guardamos y cargamos varios objetos en un fichero 
                                     con shelve.dump y pickle.load """

import shelve
cosas = ["lampara", "pantalla", "teclado"]
mascosas = ["telefono", "altavoz", "lapiz"]
fichero = shelve.open("datos_2.dat")
fichero["cosas"] = cosas
fichero["mascosas"] = mascosas
fichero.close()

fichero = shelve.open("datos_2.dat")
print fichero["cosas"]
print fichero["mascosas"]

## Finalmente borramos los ficheros con el método remove de os
import os
os.remove('datos.dat')
os.remove('datos_2.dat')

## ¿Mucho mejor verdad?