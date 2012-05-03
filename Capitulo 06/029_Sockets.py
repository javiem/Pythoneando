#!/usr/bin/python
#coding=utf-8
print "\n### Sockets ###\n"

## Cuando hablamos de sockets estamos hablando 
## fundamentalmente de comunicación entre 
## programas informáticos, posiblmente a través 
## de Internet o de la red local

## En esta comunicación hay un flujo de datos
## más o menos fiable, dependiendo del protocolo
## que se implemente, a través de las direcciones
## IP de los equipos

## Por ejemplo, el protocolo TCP es un protocolo
## fiable, con un método 3-way handshake o
## SYN,SYN-ACK,ACK que asegura que no se pierden
## datos mientras se da una comunicación, ya que
## hay un aviso entre origen y destino, es decir,
## el destino sabe que va a recibir unos datos

## En contra tenemos el protocolo UDP, un protocolo
## un poco más salvaje y no fiable que permite enviar
## datagramas sin establecer una conexión previa

## Vamos a ver como crear una conexión entre una 
## máquina servidor y una máquina cliente con Python

## El ejemplo ilustra un servidor simple con una 
## única implementación que devuelve lo recibido
## por un puerto 9999, si el texto recibido es "exit" 
## finaliza la conexión

###########################################################
############# CÓDIGO DEL SERVIDOR server.py ###############
###########  Ejecutarlo antes que el cliente  #############
###########################################################

import socket

s = socket.socket() # Creamos el objeto socket para 
                    # el servidor
                    
s.bind(("localhost", 9999)) # Para un socket de tipo
                    # IP podemos pasarle un parámetro
                    # de tipo tupla con el host y el 
                    # puerto, con ésto el servidor local
                    # quedará escuchando el puerto 9999
                    
s.listen(1) # Ahora tenemos que indicar al servidor el
            # número máximo de conexiones que podrá aceptar
            
sc, addr = s.accept() # En este punto el servidor se queda
                    # a la espera esperando alguna conexión
                    # sc corresponde al socket cliente y addr
                    # será una tupla que contendrá información
                    # del cliente, su IP y el puerto desde el 
                    # que se conecta
                    
print "Cliente conectado"
print addr 

# En este punto creamos un bucle para ir leyendo el buffer hasta
# que nos salgamos manualmente al recibir el texto "exit"
while True:
      recibido = sc.recv(1024) # Con el método recv podemos 
                        # recibir mensajes desde el cliente
                        # 1024 indica el número máximo de bytes
                        # que podemos aceptar de una sola vez
                        
      if recibido == "exit":# Si recibimos el mensaje exit 
                        # nos salimos del bucle y paramos
                        # el servicio
                        break
     
      print "Datos recibidos:", recibido # Lo mostramos
      sc.send(recibido) # Lo reenviamos, aunque no sirve 
                        # de nada, pues nuestro cliente no
                        # tiene implementado ningún método 
                        # para leer su buffer
                        
print "Cerrando"
sc.close() # Cerramos el socket del cliente
s.close() # Cerramos el socket del server

##############################################################
############## CÓDIGO DEL CLIENTE cliente.py #################
###########  Ejecutarlo por separado del server  #############
##############################################################

import socket  
s = socket.socket()  
s.connect(("localhost", 9999))  
while True:  
    mensaje = raw_input(">")  # En vez de recibir del
                    # buffer, el cliente es quien envía
                    # un texto capturado con el teclado
                    
    s.send(mensaje)  
    if mensaje == "exit": # Si escribimos exit nos 
                          # salimos del bucle y del 
                          # programa  
        break  
print "adios"
s.close() # Cerramos el socket

## Más información sobre sockets en general: 
## - http://es.wikipedia.org/wiki/Socket_de_Internet
## Y en la documentación de python:
## . http://docs.python.org/library/socket.html