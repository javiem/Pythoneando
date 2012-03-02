#!/usr/bin/python
#coding=utf-

import time

def bucle(t = 8.0):
    
    if t > 0.05:
        t = t/2.0
        
    time.sleep(t)
    print "HOMBRE BUCLE: Correcto me llaman Bucle"
    time.sleep(t)
    print "PRESENTADOR: ¿Y nos puede explicar porqué?"
    time.sleep(t)
    print "HOMBRE BUCLE: Pronto se dará cuenta"
    time.sleep(t)
    print "PRESENTADOR: ¿Me daré cuenta de que le llaman Bucle?"
    time.sleep(t)
    bucle(t)

######           Vídeo online del Hombre Bucle          ######
######    http://www.youtube.com/watch?v=1sbf5znBhuA    ######

print "\n### En honor al Hombre Bucle de Muchachada Nui ###"
print """\nPRESENTADOR: Nuestro siguiente y último protagonista viene de Torrevieja 
y su nombre es Eloy Usma, aunque sus amigos le llaman Señor Bucle. 
¿No es así Eloy?"""
time.sleep(4)  
bucle()