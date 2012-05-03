#!/usr/bin/python
#coding=utf-8
print "\n### Doctest ###\n"

## Podemos crear un sencillo juego de pruebas para una función 
## creando en el docstring un contexto de ejecución y comprobación

## Para indicar ese contexto, las líneas de ejecución empezarán con
## >>> , las líneas de resultado no necesitan empezar con >>>

## En la primera línea definimos una lista con los valores de testeo
## En la segunda llamamos a la función
## En la tercera definiremos el resultado correcto de la lista

def doblar(lista):
    """Devuelve una lista con el doble de los objetes que entran
    >>> l = [0, -4, 'AB', [1,3]]
    >>> doblar(l)
    [0, -8, 'ABAB', [1, 3, 1, 3]]
    """
    return [n * 2 for n in lista]

## Ahora definimos la función _test que ejecutará doctest
def _test():
    import doctest
    doctest.testmod()
    
## Que se llamará siempre que ejecutemos el método main al compilar
if __name__ == "__main__":
    _test()
    
## Si compilamos el fichero y no se queja será porque supera el test,
## en cambio si hay algun problema se mostrará todo el proceso de pruebas

## Podemos pasar el parámetro -v al compilar para ver la ejecución
## de las pruebas mientras se van ejecutando:
## python 036_Doctest.py -v