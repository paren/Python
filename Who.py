import getpass
import os
import sys

class Who:

    """
    Este Metodo detecta quien eres en el sesion actual,
    Si detecta el user ROOT se detiene. 
    """

    user = getpass.getuser()
    localhost = os.popen('hostname', 'r')
    localhost = localhost.read()
    sistema_operativo = os.name

    def identificar(self, user, local_host):
         
         if user == 'root':
             print ''
             print 'Usuario ' + user.upper() + ' detectado!'
             print ''
             print 'Este programa no requiere de privilegios elevados'
             print 'Cambia el usuario y reinicia'
             print ''
             sys.exit(0)

         else:
             print 'No estas usando root'
             print ''
             print 'User: ' + user
             print 'Host: ' + local_host

    #Metodo para detectar el OS, en caso de no encontrar alguno valido imprime el que encontro

    def sistema(self, SistemaOperativo, quietMode):
        if quietMode:
            return SistemaOperativo
        else:
            if SistemaOperativo == 'nt':
                print 'Sistema Windows'
            elif SistemaOperativo == 'posix':
                print 'Linux o variante Unix'
            elif SistemaOperativo == 'mac':
                print 'Mac'
            else:
                print SistemaOperativo
        



