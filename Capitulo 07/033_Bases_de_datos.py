#!/usr/bin/python
#coding=utf-8
print "\n### Bases de datos ###\n"

## Este es un tema muy amplio. Me limitaré a explicar como realizar
## algunas consultas a una base de datos sqlite

## Para más información sobre implementar persistencia con bases de
## de datos está la documentación oficial de la Database API 
## http://www.python.org/dev/peps/pep-0249/ y algunas ejemplos
## en la docu de python http://docs.python.org/library/sqlite3.html 


## A diferencia del manejo de objetos en ficheros, las bases de datos
## nos ofrecen una forma más profesional de manejar nuestros datos

## SQLite es una base de datos SQL simple y eficaz que no requiere
## previa configuración y que se basa en un solo fichero

""" Crear base de datos SQLite con una tabla, insertar y consultar
                                    los datos guardados """

# Empezamos importando la librería de manejo sqlite
import sqlite3 

database = sqlite3.connect("database.sqlite") # Nos conectamos a la base de
                            # datos, si no existe el fichero se crea
                            # automáticamente
                            
cursor = database.cursor() # Definimos el cursor. Es el objeto con que nos
                       # moveremos por la base de datos en todo momento
                        
cursor.execute("create table coordenadas (x int, y int)") # Creamos una 
                    # tabla ejecutando la consulta con el método execute 
                    # del cursor utilizando sintaxis SQL
   
# Ahora introducimos algunas coordenadas de una colección en la tabla            
coordenadas = [(30, 0),
               (15, -3),
               (0, 0)]  

# Los podemos hacer utilizando el método executemany
cursor.executemany("insert into coordenadas ('x', 'y') values (?,?)", 
                               coordenadas)

database.commit() # Con el método commit confirmamos todos los canvios

cursor.execute("select * from coordenadas") # Creamos una consulta para 
                                            # leer las coordenadas
                                            
for coordenada in cursor.fetchall(): # Con el método fetchall sacamos los 
    print coordenada                 # resultados en forma de tupla  
    
## Podemos hacer la consulta más rápido en dos líneas
for row in cursor.execute('select * from coordenadas'):
    print row
        
## Antes de cerrar el programa cerramos el cursor y la conexión
cursor.close()
database.close()
        
# Finalmente borramos el fichero con la base de datos
import os
os.remove('database.sqlite')