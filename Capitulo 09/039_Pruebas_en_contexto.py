#!/usr/bin/python
#coding=utf-8
print "\n### Pruebas en contexto con Unittest ###\n"

## Con unittest podemos preparar un entorno dónde ejecutar las pruebas

## Ya sea preparar un archivo, introducir valores en una base de datos, 
## o conectarse a otra máquina. Esto se conoce como test fixture o
## sistema de testeo a medida -> http://en.wikipedia.org/wiki/Test_fixture

## TestCase tiene dos métodos para preparar el entorno. Son
## setUp y tearDown y se llaman al inicio y fin del contexto

import unittest

def doble(obj):
    """Devuelve el doble de un objeto"""
    return obj * 2

class PruebasEnContexto(unittest.TestCase):
    
    def setUp(self):
        print "Preparando contexto"
        self.lista = [0, -4, 'AB', [1,3]]
        
    def test(self):
        print "Ejecutando test de comprobación"
        r = [doble(o) for o in self.lista]
        self.assertEqual(r, [0, -8, 'ABAB', [1, 3, 1, 3]], msg="El test de comprobación falló")
        
    def tearDown(self):
        print "Desconstruyendo contexto"
        del self.lista
        
if __name__ == "__main__":
    unittest.main()
