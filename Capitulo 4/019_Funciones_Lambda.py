#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Funciones lambda ###\n"

## Las funciones lamba de Python son funciones anónimas en tiempo
## de ejecución, es decir, se declaran y se usan en el momento
## Están limitadas a una sola expresión y se utilizan junto a las
## iteraciones de orden superior para acortar código

# Función normal

def doble(numero) :
    return numero*2

print doble(5)

# Función lamba
doble = lambda x: x*2

print doble(5)

# Mapeo con función normal
def triple(numero) :
    return numero*3
lista = [1, 2, 3, 4, 5]
listaPor3 = map(triple, lista)
print listaPor3

# Mapeo con función lambda
lista = [1, 2, 3, 4, 5]
print map(lambda x: x * 3, lista)

## Como vemos la reducción de código es notable
## El inconveniente es que la función se declara 
## y se usa en el momento

## Se puede utilizar cualquier iteración de orden 
## superior con las funciones lambda

# Reducción a suma total
lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print reduce(lambda x, y: x + y, lista)

# Filtro múltiples de tres
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print filter(lambda x: x%3 == 0, lista)

