#!/usr/bin/python

print "\n### Colecciones 1: Listas ###"

# Son los arrays o vectores de Python y son muy flexibles
# Pueden contenter cualquier tipo de dato, incluso otras listas

lista = [1, 0x13, False, "Una cadena de texto", [1, 7.0]]

print lista[1], type(lista[1])
print lista[3], type(lista[3])
print lista[4], type(lista[4])

# Elemento de una lista multidimensional
print lista[4][1], type(lista[4][1])

# Modificar un elemento
lista[0] = 99;
print lista[1], type(lista[1])

# Accediendo al ultimo elemento
print lista[-1]

# Slicing => Particionado de seleccion (inicio:fin) el final no entra
print lista[0:3]

# Slicing con salto (inicio:fin:salto) cada cuanto seleccionar el elemento
print lista[0:5:2]

# Valores por defecto de inicio y fin
print lista[::2]

