#!/usr/bin/python

print "\n### Condicionales ###"

# IF

nota = 10

if nota == 10 :
    print "Has sacado un 10"
    print "Puntuacion perfecta"
    
# IF-ELSE

nota = 7

if nota >= 5 :
    print "Felicidades has aprobado con un" , nota
else :
    print "Has suspendido con un" , nota

# IF-ELIF-ELSE

nota = 4

if nota > 9 :
    print "Has sacado un sobresaliente"
    print "Buen trabajo"
elif nota >= 5 :
    print "Has sacado un" , nota
    print "Podrias haberlo hecho mejor" 
else :
    print "Has sacado un" , nota
    print "Menudo desastre"
    
# A IF C ELSE B
# Si C entonces A sino B

nota = 5

print "Aprobado" if (nota >= 5) else "Suspendido"

    