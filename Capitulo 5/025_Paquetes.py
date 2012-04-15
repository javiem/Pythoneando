#!/usr/bin/python
#coding=utf-8
print "\n### Paquetes ###\n"

### Los paquetes son útiles para organizar los 
### módulos de nuestros programas

## Para usarlos tenemos que crear el fichero __init__.py
## en el directorio con nuestros módulos, así tendremos un
## paquete nuevo. Para importar módulos de un paquete
## usaríamos la sintaxis siguiente:

### <nombre_paquete>.<nombre_modulo> import <Clases>

from paquete.modulo import MiClase
c = MiClase()