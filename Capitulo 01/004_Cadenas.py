#!/usr/bin/python
#coding=utf-8

print "\n### Cadenas de texto ###"

# cadenas normales
c = 'áèïóù'
print "áèïóù" , type(c)
# cadenas unicode
c = u'áèïóù'
print "u'áèïóù'" , type(c)
# cadenas raw
r = r"\n"
print "r\"\\n\"= " + r

# cadenas con varias lineas triple comilla
s = """
         Ésto
     parece texto
       centrado
    """
print s

# concatenar y multiplicar cadenas

c1 = "Hola"
c2 = " Mundo "
s = c1 + c2
print s

s = (c1 + c2) * 3
print s