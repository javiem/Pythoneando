#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Expresiones generadoras ###\n"

## Devuelven generadores en lugar de listas
## Generan valores sobre los que iterar

l = [1,2,3]
n = 3

# Lista
c = [n * 2 for n in l]
print c

# Generador
g = (n * 2 for n in l)
print g

# Recorrer los valores del generador
for n in g:
    print n

# Una función generadora que devuelve el valor sobre el 
# que itera utilizando la palabra yield
def generador(n,m,s):
    while (n <= m):
        yield n
        n+= s

x = generador(0,5,1)
print x

for n in generador(0,5,1):
    print n
    
# Se puede transformar un generador a una lista utilizando list
lista = list(generador(0,5,1))
print lista