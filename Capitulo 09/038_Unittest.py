#!/usr/bin/python
#coding=utf-8
print "\n### Unittest ###\n"

## Unittest/PyUnit es una versión Python de la librería de testeo
## de Java JUnit especializada en tests unitarios
## Documentación: http://docs.python.org/library/unittest.html

def doble(obj):
    """Devuelve el doble de un objeto"""
    return obj * 2

## Para hacer el juego de pruebas hay que crear una clase hija
## de unittest.TestCase y dentro declarar todos los test que queramos
## como métodos. La norma que deben cumplir es empezar con test
## Al llamar a unittest.main() se ejecutaran todos los métodos de las
## clases hijas de unittest.TestCase

import unittest

class Pruebas(unittest.TestCase):
    def test(self):
        l = [0, -4, 'AB', [1,3]]
        r = [doble(o) for o in l]
        ## asserEqual es un método que comprueba que una
        ## variable sea equivalente a otra
        ## El parámetro opcional msg permite mostrar un texto si falla
        ## devolviendo > AssertionError: El test de comprobación falló
        self.assertEqual(r, [0, -8, 'ABAB', [1, 3, 1, 3]], msg="El test de comprobación falló")
        ## Una lista de métodos disponibles se encuentra en la docu
        ## http://docs.python.org/library/unittest.html#assert-methods
        
if __name__ == "__main__":
    unittest.main()
    
## Si el test se ejecuta correctamente se muestra un OK