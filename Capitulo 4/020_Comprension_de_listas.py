#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Comprensión de listas ###\n"

## Es una forma de utilizar la comprensión lógica en las listas
## en vez de las iteraciones de orden superior y las funciones lambda
## Se trata de traspasar la lógica matemática a la mismísima 
## declaración de nuestros objetos

## EJEMPLO 1: Crear una lista con cuadrados

# Método append con for in
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print cuadrados

# Método map con lambda
cuadrados = map(lambda x: x**2, range(10))
print cuadrados

# Método con comprensión de listas
# En la propia declaración se añade la iteración para crear la lista
cuadrados = [x**2 for x in range(10)]
print cuadrados

## EJEMPLO 2: Crear una lista de coordenadas dónde se cumple 
## que x != y a partir de dos vectores

coordenadas = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]
print coordenadas

# Lo anterior equivaldría a dos for con condición anidados
coords = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            coords.append((x,y))
print coords

## EJEMPLO 3: Filtros de comprensión

vector = [-4,-2,0,2,4]
# Mostramos la lista excluyendo los negativos
print [x for x in vector if x >= 0]
# Mostramos la lista doblada
print [x*2 for x in vector]
# Mostramos la lista con valores absolutos
print [abs(x) for x in vector]

## EJEMPLO 4: Con métodos sobre cadenas de texto

frutaFresca = ['      platano  ', '    manzana ', '   limon  ']
print [fruta.split() for fruta in frutaFresca]

## EJEMPLo 5: Generando coordenadas es importante el uso de los paréntisis

print [(x, x**2) for x in range(6)]

## EJEMPLO 6: Crear un único vector de una lista con varios vectores 
vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]

## EJEMPLO 7: Crear una matriz 3*3 a partir de una 4*4 en una sola línea

matriz = [ [ 1, 2, 3, 4 ],
           [ 5, 6, 7, 8 ],
           [ 9, 10, 11, 12] ]

print [[fila[i] for fila in matriz] for i in range(4)]

# Equivalente con for

nueva_matriz = []
for i in range(4):
    nueva_matriz.append([fila[i] for fila in matriz])
print nueva_matriz