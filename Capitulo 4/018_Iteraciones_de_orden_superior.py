#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Iteraciones de orden superior ###\n"

## MAP: Mapeo de listas. Con él podemos ejecutar una 
## función sobre todos los elementos de una lista

def doble(numero) :
    return numero*2

lista = [1, 2, 3, 4, 5]

listaPor2 = map(doble, lista)

print lista
print listaPor2

## FILTER: Filtro de secuencias con funciones 
def esPar(numero):
    if numero % 2.0 == 0 : 
        return True
    else :
        return False

numeros = [1,2,3,4,5,6,7,8,9,10]
    
pares = filter(esPar, numeros)

print numeros
print pares

## REDUCE: Ejecuta una función reductura a todos los elementos 
## de una lista. Por ejemplo sumar todos los elementos.

def suma(x, y):
    return x+y

lista = [1,2,3,4,5,6,7,8,9,10]
sumaTotal = reduce(suma, lista)

print lista
print sumaTotal

