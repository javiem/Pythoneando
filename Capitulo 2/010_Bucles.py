#!/usr/bin/python

print "\n### Bucles ###"

# WHILE
segundos = 5
while segundos > 0 :
    print "La bomba explotara en", segundos , "segundos"
    segundos = segundos - 1
print "BOOOOOOM!!!"
        
# BUCLE CON CONTINUE
numero = 1
while numero <= 10:
    numero = numero + 1
    if numero % 2 != 0:
        # si el numero no es par pasamos al siguiente sin mostrar nada
        continue
    print numero, "es par"

# FOR ... IN (foreach de php)

frutero = ["limon", "naranja", "manzana"]
for fruta in frutero :
    print fruta
    
# FOR CON ACUMULADOR

for i in range(5):
  print i,
  

# FOR ANIDADO EN FOR CON CONDICIONALES
for x in range(5):
    print "\n",
    for y in range(5):
        if y == 0 or y == 4:
            print "#",
        elif x == 0 or x == 4:
            print "#",
        else: 
            print " ",
        