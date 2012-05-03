#!/usr/bin/python

print "\n### Funciones ###"

def operaciones(num1, num2):
    print "Serie de operaciones para los numeros", num1, "y", num2
    print num1 , " + ", num2 , " = ", num1+num2
    print num1 , " - ", num2 , " = ", num1-num2    
    print num1 , " * ", num2 , " = ", num1*num2
    
    # "and" es un operador logico que indica una comparacion Y
    # tambien existe el "or" que es un O y el "not" para negar
    # aqui comprobamos que ninguno de los dos numeros sea un cero
    # ya que eso haria una division que daria error
    
    if (num1 != 0 and num2 != 0) :
        print num1 , " / ", num2 , " = ", float(num1)/float(num2)  
          
operaciones(1,5)
operaciones(num2=1, num1=5)


# Funciones con parametros predefindos
def numeroYcolor(numero = 5, color = "azul"):
    print "Numero", numero, "y color", color
    
numeroYcolor() #valores por defecto
numeroYcolor(10) #afecta al primer argumento
numeroYcolor(color="verde") #afecta al segundo
numeroYcolor(7, "rojo")

# Funciones con parametros indefinidos
def indefinidos(*args):
    #*args es una tupla
    for param in args:
        print param
    
indefinidos(1, "texto", 8.56)

def mas_indefinidos(**args):
    #*args es un diccionario
    for param in args.items():
        print param
    
mas_indefinidos(uno = 1, dos = 2, tres = 3)

# Devolviendo datos
def doble(num1):
    return num1*2

print "El doble de 5 es", doble(5)

# Devolviendo tuplas
def dobleYmitad(num1):
    return num1*2, float(num1)/2
    
print "El doble y la mitad de 5 son" , dobleYmitad(5)
