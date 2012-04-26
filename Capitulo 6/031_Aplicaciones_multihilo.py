#!/usr/bin/python
#coding=utf-8
print "\n### Aplicaciones multihilo ###\n"

## En este preciso instante es más que seguro que tu 
## máquina está ejecutando muchísimos procesos a la vez
## sin quejarse ni una pizca, y siento decepcionaros si
## digo que no tiene nada que ver con el número de cores
## de vuestro procesador... bueno, quizá un poquito

## En resumidas cuentas todos los procesos de la máquina
## pasan por una cola de prioridades. Estos procesos se 
## ejecutan durante unos instantes cada uno y nos dan el
## efecto de ser continuados, aunque no es así

## Multihilo es un concepto por el cual una aplicación puede   
## tomar varios caminos en un momento dado sin pararse 
## ejecutar uno de ellos antes que el otro...
## ¡Cómo mirar a la izquierda y a la derecha a la vez!

## El ejemplo más claro para ver el funcionamiento de los 
## threads es siempre parecido... Crear un thread padre y 
## ejecutar sus hijos mientras éste está en marcha

# Tomemos por thread padre al propio flujo de la aplicación

import threading
class MiThread(threading.Thread):
      def __init__(self, num):
          threading.Thread.__init__(self)
          self.num = num
      def run(self): # Se ejecuta automáticamente
          print "Soy el hijo", self.num
          
print "Soy el padre"
for i in range(0, 5):
    t = MiThread(i)
    t.start()
    t.join() # Indica que el padre no finalice antes que los hijos
    
## Vale, ésto es demasiado rápido para verlo, pero, y si modificamos
## nuestro hilo para que haga alguna pausas y nos recorra una lista?

import time

class MiThreadConPausas(threading.Thread):
      def __init__(self, num):
          threading.Thread.__init__(self)
          self.num = num
      def run(self): # Se ejecuta automáticamente
          for n in range(0,2):
              time.sleep(1)
          print "Thread %d finalizado" % self.num
              
print "Soy el padre"
for i in range(0, 5):
    t = MiThreadConPausas(i)
    t.start()
    print "Hilos en ejecucion: %d"  % threading.activeCount()   
    t.join()  # si probáis sin el join veréis como todos los thread
                    # se ejecutan a la vez   

# Más adelante volveré a hablar de hilos y cómo manejar variables globales