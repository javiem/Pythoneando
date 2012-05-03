#!/usr/bin/python
#coding=utf-8
print "\n### Peticiones a webs ###\n"

## El libro de Python para todos que sigo para ir
## aprendiendo el lenguaje Python toca el tema de
## la interacción con webs enseñando un poco las
## librerías urllib y urllib2

## Personalmente no las conozco pero si he hecho
## cosas con la librería cURL en php y estoy seguro
## que hay alguna versión para Python, así que haré
## algunos ejercicios más adelante con ella 

## De momento pondré algun ejemplo de como utilizar
## urllib2 y lo que se puede conseguir con esa librería
## que incluye python

## Con el siguiente bloque podemos leer una página entera
## y visualizar su código tal cual lo interpreta nuestro 
## navegador de Internet

import urllib2

try:
    f = urllib2.urlopen("http://www.hcosta.info") # Crea la
                                        # petición a la url
                                        
    print f.read() # Muestra el contenido como  
                # si de un fichero se tratase
                
    f.close() # Cierra el fichero

# Tratamos las excepciones  
except HTTPError, e:
    print "Ocurrió un error"
    print e.code
except URLError, e:
    print "Ocurrió un error"
    print e.reason
    
## Se pueden hacer otras cosas como peticiones POST y GET,
## editar las cabeceras o utilizar autenticación. emular 
## cookies... Lo dejamos para más adelante

## Más información y ejemplo de la librería urllib2 en:
## - http://docs.python.org/library/urllib2.html
