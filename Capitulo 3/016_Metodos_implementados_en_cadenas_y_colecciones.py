#!/usr/bin/python
#coding=utf-8
print "\n### Programacion Orientada a Objetos: Revisión de objetos ###\n"

####
#### CADENAS
####

## LOWER: Transforma la cadena a minúsculas
frase = "De acuerdo. Nos reunimos a las diez."
print frase.lower()

## UPPER: Transforma la cadena a mayúsculas
print frase.upper()

## COUNT(s, inicio, fin): Busca una subcadena en una cadena
## se pueden especificar los puntos entre los que buscar
cadena = "hola lola mola la trola"
# veces que aparece "ola" en toda la cadena
print cadena.count("ola")
# veces que aparece "ola" del carácter 10 (0-9) hasta el final
print cadena.count("ola", 9, len(cadena))

## FIND(s, inicio, fin): Busca el índice dónde aparece por
## primera vez una subcadena, se pueden especificar los puntos 
## entre los que buscar
print cadena.find("ola")
print cadena.find("ola", 9, len(cadena))

## RFIND(s, inicio, fin): Busca el índice dónde aparece por
## última vez una subcadena, se pueden especificar los puntos 
## entre los que buscar
print cadena.rfind("ola")
print cadena.rfind("ola", 0, len(cadena)/2)

## JOIN: Combina los elementos de un array de cadenas con otra cadena
letras = ['a','b','c','d','e','f']
separador = ","
print separador.join(letras)

## PARTITION: Busca el separador y devuelve una tupla con los elementos
## hasta el primer separador, el separador en sí, y los elementos restantes
cadena_unida = separador.join(letras)
print cadena_unida.partition(separador)

## SPLIT(separador, maximo): Busca el separador de una cadena y 
## crea una lista con todas las subcadenas separadas
## Se puede indicar un máximo de subcadenas a separar
print cadena_unida.split(",")

## STRIP(c): Borra el carácter o subcadena indicada del principio y final
## Si no se le pasa nada, intenta borrar los espacios en blanco
frase = "    Hola Mundo    "
print frase
print frase.strip()
frase = "Hola Mundo"
print frase.strip("H")

## REPLACE(vieja, nueva, maximo): Devuelve una cadena en la que se 
## substituyen las ocurrencias de la cadena nueva en la vieja
## Se puede indicar un máximo de substituciones
palabra_muy_larga = "electroencefalografista"
print palabra_muy_larga.replace("e","E")
print palabra_muy_larga.replace("e","E", 1)

####
#### LISTAS
####

lista = [1, 2, False, "Una cadena de texto", [1, 7.0]]
print lista

## APPEND(objeto): Añade un objeto al final de la lista
lista.append("Otra cadena")
print lista

## COUNT(valor): Devuelve el número de veces que se repite un valor
lista.append(1)
print lista
print lista.count(1)

## EXTEND(iterable): Añade los elementos de una coleccion a la lista
lista2 = [2,3,"otro texto"]
lista.extend(lista2)
print lista
## INDEX(valor, principio, fin): Devuelve la posición en la que se encontró la primera 
## ocurrencia de un valor. Se pueden especificar los puntos 
## entre los que buscar
print lista.index(3)

## INSERT(index, objeto): Inserta el objeto object en la posición index
lista.insert(0, "Primer elemento")
print lista

## POP(index): Devuelve el valor en la posición index y lo elimina de la 
## lista. Si no se especifica la posición, se utiliza el último 
## elemento de la lista
lista.pop()
lista.pop(0)
print lista

## REMOVE(valor): Eliminar la primera ocurrencia de value en la lista
lista.remove(1)
print lista

## REVERSE: Invierte la lista.
lista.reverse()
print lista

## SORT(cmp=None, key=None, reverse=False): Ordena la lista utilizando 
## el típico algoritmo comparativo de -1, 0 , 1. Si se le pasa reverse 
## True la ordena del revés y la key debe ser una función que a partir
## de un elemento de la lista devuelva una clave para la comparación.

numeros = [1,6,3,8,5,9,4,0,7,2]
print numeros
numeros.sort()
print numeros

numeros = [1,6,3,8,5,9,4,0,7,2]
numeros.sort(reverse=True)
print numeros

####
#### DICCIONARIOS
####

meses = {1 : "Enero",
         2 : "Febrero",
         3 : "Marzo" }

## GET: Busca el valor de una clave, puede dar 
## un valor por defecto si no se encuentra nada
print meses.get(1,"No existe")
print meses.get(4,"No existe")

## HAS_KEY: Verifica si existe una clave
print meses.has_key(1)
print meses.has_key(4)

## ITEMS: Devuelve una lista de tuplas clave-valor
print meses.items()

## KEYS: Devuelve una lista de las claves
print meses.keys()

## VALUES: Devuelve una lista de los valores
print meses.values()

## POP: Borra una clave y devuelve el valor. Puede
## dar un valor por defecto si no se encuentra nada.

print meses.pop(3,"No se encontró")
print meses.pop(3,"No se encontró")
print meses.items()

## CLEAR: Vacía el diccionario sin borrarlo 

meses.clear()
print meses.items()