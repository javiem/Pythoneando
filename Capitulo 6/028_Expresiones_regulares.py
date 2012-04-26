#!/usr/bin/python
#coding=utf-8
print "\n### Expresiones regulares ###\n"

## Son patrones que sirven para filtrar cadenas de texto
## Muy útiles para hacer comprobaciones de muchos tipos

## El módulo re nos proporciona las herramientas para trabajar 
## con las expresiones regulares:
## http://docs.python.org/library/re.html
import re

## Un primer y sencillo ejemplo nos mostrará su utilidad

## comprobamos si en una cadena "puente" coincide con la expresión
## regular "puente"
if re.match("puente", "puente"):
    print "cierto"
    
## De acuerdo, no es muy sorprendente, pero y si quisiéramos 
## comprobar que una palabra tiene exactamente 6 carácteres y 
## acaba en -uente?
if re.match(".uente", "puente"):
    print "cierto"
    
## El punto significa precisamente que en esa posición
## puede haber cualquier carácter, pero solo uno

## Si queremos comprobar por ejemplo si una cadena es una
## extensión de un archivo, podemos hacerlo con 4 puntos!
## pero hay que escapar el primero con la barra invertida
if re.match("\....", ".mp4"):
    print "es extension"
    
## Imaginad que tenemos una serie de palabra muy parecidas
## Si queremos comprobar si se cumple una condición en todas 
## ellas podemos crear un grupo

## Por ejemplo, si una de las palabras de la expresión 
## regular es igual que la cadena
if re.match("siente|puente|diente", "diente"):
    print "es igual"
    
## También funcionaría sacando la parte común fuera
if re.match("(si|pu|di)ente", "diente"):
    print "es igual"   
    
## Incluso se puede crear una pequeña lista de carácteres []
## que comprobaria las palabras siente, diente, miente
if re.match("[sdm]iente", "diente"):
    print "es igual"      
    
## Tambien podemos crear pequeñas listas de carácteres o números 
## que abarquen todo el abecedario o los números naturales
## con la sintaxis [a-z] o [0-9]

## Hay que tener en cuenta que estas pequeñas listas son sensibles
## a mayúsculas y minúsculas, por lo que si queremos comprobar que
## una tiene una mayúsculas en alguna posición usaríamos [A-Z]

## Además podemos concatenar conjuntos, por ejemplo [a-zA-Z0-9]
## comprobaría que un carácter sea una letra o un número

## Si quisieramos comprobar un carácter especial con el método 
## de los corchetes no haría falta escaparlo
if re.match("[.]...", ".mp4"):
    print "es extension"

## Podemos negar los conjuntos de carácteres con el carácter sombrero 
## [^] Por lo que la siguiente sentencia sería cierta
if re.match("[^a-zA-Z0-9]...", ".mp4"):
    print "es extension"
    
## Todo esto es muy bonito pero nada práctico, es obvio.
## La verdad es que los conjuntos de carácteres ya estan definidos
## en las expresiones regulares, así que utilizando una sintaxis
## ya definida podemos hacer este tipo de comprobaciones fácilmente

### "\d" : dígito, equivale a -> [0-9]
### "\D" : carácter no dígito -> [^ 0-9]
### "\w" : carácter alfanumérico [a-zA-Z-0-9_]
### "\W" : carácter no alfanumérico [^ a-zA-Z-0-9_]
### "\s" : carácter en blanco [ \t\n\r\f\v]
### "\S" : carácter no blanco. [^ \t\n\r\f\v]

if re.match("[.]\w\w\w", ".mp4"):
    print "es extension"
    
## De todas formas esto no es muy útil, si hubiera alguna forma de 
## comprobar esas tres letras repetidas fácilmente... ¿he dicho repetir? 

## El módulo re también nos permite analizar repeticiones de carácteres

## Hay unos carácteres especiales y reservados: '+' , '*' y '?' que junto
## a las llaves {} nos van a permitir analizar una cadena hasta donde 
## nuestra imaginación nos permita :)

## '+': comprueba si se repite el último dígito a la izquierda, necesita
## almenos una repetición
if re.match("ho+la", "hoooooola"):
    print "se repite"
    
## '*': comprueba si se repite el último dígito a la izquierda, no cuenta
## la primera repetición
if re.match("ho*la", "hla"):
    print "verdadero"
    
## '?': indica opcionalidad, está el caràcter de la izquierda o not
if re.match("home-?brew", "homebrew"):
    print "si está"
    
if re.match("home-?brew", "home-brew"):
    print "si está"
    
## '{}': con las llaves indicamos el número exacto de veces que se puede 
## repetir el carácter de la izquierda
if re.match("ho{3}la", "hooola"):
    print "verdadero"
    
## Con la coma indicamos el número de repeticiones mínimo
if re.match("ho{3,}la", "hooooooola"):
    print "verdadero"
    
## Con el rango {x,y} se indica un número de repeticions mínimo y máximo
if re.match("ho{0,4}la", "hla"):
    print "verdadero"
    
### Ahora que nos hemos familiarizado con las expresiones regulares
### vamos a ver cómo hacer filtros más sofisticados combinando lo que
### sabemos y algo más

## Comprobar si una cadena es un enlace web
## Analizamos el principio de la cadena seguido de un número
## cualquiera de carácteres y el final de la cadena 
if re.match("http://.+\.info", "http://www.hcosta.info"):
    print "es web"
    
## Si capturasemos lo que retorna re en ese ejemplo podríamos obtener
## lo que se conoce como un matchObject

## El matchObject tiene un método llamado group() con el cuál podemos
## analizar las partes en que queda partida nuestra string después
## de pasarle las expresiones regulares
o = re.match("http://.+\.info", "http://hcosta.info")
print o.group(0) # Aquí devuelve sólamente una parte

## Pero si utilizamos los paréntesis
o = re.match("http://(.+)\.info", "http://hcosta.info")
print o.group(1) # En la posición 2 del group bemos como queda partido
                 # el dominio -> hcosta
                 
## El método groups() devuelve todas las partes: ('hcosta', 'info')
o = re.match("http://(.+)\.(.{4})", "http://hcosta.info")
print o.groups()

## E incluso podríamos llegar a... ('www', 'hcosta', 'info')
o = re.match("http://(.+)\.(.+)\.(.{4})", "http://www.hcosta.info")
print o.groups()

## Con lo que sabemos seguro que seríamos capaces de verificar si un email
## contiene almenos 3 caràcteres de dirección, una @ y un dominio de 3 caràcteres
o = re.match("(.{3,})@(.{3,})\.(.{2,})", "ejemplo@email.com")
if o:
    print "ejemplo@email.com es válido"
    print o.groups()
else:
    print "ejemplo@email.com no es valido"

o = re.match("(.{3,})@(.{3,})\.(.{2,})", "10@mail.co")
if o:
    print "10@mail.co es válido"
    print o.groups()
else:
    print "10@mail.co no es valido"

## Hasta aquí llega mi explicación, pero las expresiones regulares nos ofrecen 
## la función match() sólo es la punta del iceberg

## Con expresiones regulares podemos realizar división de cadenas por patrones,
## substuir cadenas con patrones... Si te interesa el tema echa una ojeada a la
## documentación oficial: http://docs.python.org/library/re.html#module-contents
 
