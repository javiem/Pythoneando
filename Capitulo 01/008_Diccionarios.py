#!/usr/bin/python

print "\n### Listas 3: Diccionarios ###"

# Los diccionarios son matrices asociativas, lo que viene a ser 
# en PHP los arrays asociativos por clave y valor que tanto me gustan
# En los diccionarios se accede al valor a traves de la clave
# A diferencia de las listas y tuplas son colecciones desordenadas

frutas = { "Naranja":"Orange",
           "Fresa":"Strawberry",
           "Manzana":"Apple" }

print "Manzana en ingles es: " + frutas["Manzana"]

# Modificando el diccionario por clave
frutas["Manzana"] = "Poma"

print "Manzana en catalan es: " + frutas["Manzana"]