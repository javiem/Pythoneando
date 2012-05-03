#!/usr/bin/python
#coding=utf-8

## Es la forma de distribuir paquetes en Python desde la versión 1.6
## Requiere un fichero setup.py

## Se instala ejecutando >python setup.py install

"""C:\Ejercicios_python\Capitulo 10\040_Distutils> python setup.py install
running install
running build
running build_scripts
creating build
creating build\scripts-2.7
copying and adjusting programa.py -> build\scripts-2.7
running install_scripts
copying build\scripts-2.7\programa.py -> C:\Python27\Scripts
running install_egg_info
Writing C:\Python27\Lib\site-packages\Distutils-1.0-py2.7.egg-info"""

## Luego si queremos crear el archivador utilizaríamos >python setup.py sdist
## que generará un zip en Windows y un     tar.gz en Unix

"""C:\Ejercicios_python\Capitulo 10\040_Distutils> python setup.py sdist
running sdist
running check
warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)
warning: sdist: standard file not found: should have one of README, README.txt
writing manifest file 'MANIFEST'
creating Distutils-1.0
copying files to Distutils-1.0...
copying programa.py -> Distutils-1.0
copying setup.py -> Distutils-1.0
creating dist
creating 'dist\Distutils-1.0.zip' and adding 'Distutils-1.0' to it
adding 'Distutils-1.0\PKG-INFO'
adding 'Distutils-1.0\programa.py'
adding 'Distutils-1.0\setup.py'
removing 'Distutils-1.0' (and everything under it)"""

## Aquí empieza el super programa
print "Esto será un programa distribuido con distutils"
## Aquí acaba el super programa