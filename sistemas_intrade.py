from Matrix import Matrix
from Who import Who
from Hostme import Hostme
from Portme import Portme
from WebGetter import FetchMe


"""
Con este programa verificaremos
que un host este en linea usando
pings.

Version 0.4

Menu para sistemas

Depencias:
    ping
    traceroute
    nmap
    whois
    dig

Bugs:

La opcion C no soporta un rango de ip.
ejemplo: 1-9999
"""

#Instanciamos las clases

#Clase Who verifica que el script no corra en super usuario
#si el script corre con Root negara el acceso
identidad = Who()
identidad
identidad.identificar(identidad.user, identidad.localhost)
identidad.sistema(identidad.sistema_operativo)

#Clase con herramientas a usar
conexion = Matrix()

# Inicia Menu
menu = ''
while menu != 'x':
    print chr(27) + "[0;36m" + 'Menu Sistemas'
    print ' '
    print 'a) Verificar un sitio o ip'
    print 'b) Ver perdida de paquetes'
    print 'c) Verificar puerto activo'
    print 'd) Verificar nombre de dominio'
    print 'e) Verificar ip publica'
    print 'f) Verificar listas negras --Beta'
    print 'g) Verificar records DNS'
    print 'x) Salir'
    print ' '
    print 'Todo url se debe consultar sin http:// al principio'
    print ' '

    menu = str(raw_input('Elija una opcion $: ')).lower() # Usando la funcion lower forzamos letra minusculas

    if menu == 'a':
        verificar = Hostme('') # a HostMe se le pasa un parametro '' para que pida host- Ver Clase
        print ''
        conexion.pingeame(verificar.host)

    elif menu == 'b':
        verificar = Hostme('')
        conexion.traceme(verificar.host)

    elif menu == 'c':
        verificar = Hostme('')
        verificar_puerto = Portme('')
        conexion.scanme(verificar.host, verificar_puerto.port)

    elif menu == 'd':
        verificar = Hostme('')
        conexion.whom(verificar.host)

    elif menu == 'e':
        print ''
        webstuff = FetchMe()
        webstuff.findip()
        print ''

    elif menu == 'f':
        print ''
        pass # Agregamos esta funcion para que no haga nada en esta opcion
        print ''

    elif menu == 'g':
        verificar = Hostme('')
        conexion.dig(verificar.host)
        
# Salida del loop while
print ' '
print 'Gracias por usar este software'
print ' '

#TODO: agregar la verificacion en lista negra
# http://www.mxtoolbox.com/SuperTool.aspx?action=blacklist%3a--aqui_nombre de dominio

