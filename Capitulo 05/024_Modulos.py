#!/usr/bin/python
#coding=utf-8
print "\n### Módulos ###\n"

### Los módulos son útiles para organizar el código de 
### nuestros programas

### Para importar un módulo utilizamos la sintaxis
import modulo_f
modulo_f.mi_funcion()

### Tambien podemos importar solo una clase de un modulo
from modulo_c import MiClase
c = MiClase()

### Se pueden importar todos los nombres de un módulo
## aunque no es muy recomendable...
from modulo_c import *
c2 = MiClase()