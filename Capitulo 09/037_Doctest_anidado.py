#!/usr/bin/python
#coding=utf-8
print "\n### Doctest con sentencias anidadas ###\n"

## Por sentencias anidadas se entiende el código de un bloque
## Por ejemplo si queremos ejecutar un bucle for, lo tendremos
## que anidas con los tres puntos ...

def doble(obj):
    """Devuelve el doble de un objeto
    >>> l = [0, -4, 'AB', [1,3]]
    >>> for o in l:
    ...     doble(o)
    0
    -8
    'ABAB'
    [1, 3, 1, 3]
    """
    return obj * 2

## Ahora definimos la función _test que ejecutará doctest
def _test():
    import doctest
    doctest.testmod()
    
## Que se llamará siempre que ejecutemos el método main al compilar
if __name__ == "__main__":
    _test()
    