#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Funciones decoradoras ###\n"

## Son funciones que reciben una función como parámetro y 
## devuelven otra función como resultado


# Por ejemplo decorador() recibe una funcion, muestra el nombre
# y devuelve el resultado en función de los parámetros que entran
def decorador(funcion):
    def nueva(*args):
        print "Llamando a la funcion", funcion.__name__
        retorno = funcion(*args)
        return retorno
    return nueva

# Ara creamos una función cualquiera
def echo(frase):
    print "::Echo: " + frase
    
# Y la sintaxis para llamar al decorador quedaría:
decorador(echo)("Hola")

# Si precedimnos la definición con @funcion_decoradora no hará
# falta llamar siempre al decorador con la sintaxis anterior

@decorador
def echo(frase):
    print "::Echo: " + frase
    
echo("Hola")