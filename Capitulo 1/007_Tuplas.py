#!/usr/bin/python

print "\n### Colecciones 2: Tuplas ###"

# Las tuplas son colecciones mas ligeras que las listas,
# una vez creadas son inmutables y su tamano no puede variar.
# Su constructor es la coma, pero se aconseja enumerarlas entre parentesis

tupla = 1, 2.0, True, "Hola Mundo", [1, 2]
print tupla, type(tupla)

# El slicing es igual que con las listas

# Accediendo al ultimo elemento
print tupla[-1]

# (inicio:fin) el final no entra
print tupla[0:3]

# (inicio:fin:salto) cada cuanto seleccionar el elemento
print tupla[0:5:2]

# Valores por defecto de inicio y fin
print tupla[::2]
