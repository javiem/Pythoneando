#!/usr/bin/python
#coding=utf-8
print "\n### Programacion funcional: Introducción ###\n"

## En python todo son objetos, incluso las funciones
## Se pueden pasar como argumentos de otra funcion
## y devolverlas como si fueran una variable más

def saludar(lang):
    def saludar_ca():
        print "Bon dia" 
               
    def saludar_es():
        print "Buenos dias"
        
    def saludar_en():
        print "Good morning"
        
    ## HAY QUE DEVOLVER LA FUNCION SIN EJECUTAR EL MÉTODO
    ## Es decir: saludar_ca y no saludar_ca()
    languages = { "ca": saludar_ca,
                  "es": saludar_es,
                  "en": saludar_en }
    
    return languages[lang]
    
s = saludar("en")
s()
