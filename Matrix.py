import Matrix
import os
from time import sleep

class Matrix:

    #Propiedades (Herramientas de trabajo)
    scanr = 'nmap'
    tracer = 'traceroute'
    ider = 'whois'
    ping = 'ping'
    diger = 'dig'

    # Metodo para hacer pings
    def pingeame(self, host):
        pinger = Matrix.ping
        verificacion_pinger = os.popen(pinger + ' ' +'-c 1 ' + ' ' + host, 'r')
        i = 0
        for line in verificacion_pinger:
            i += 1
            if i == 5:
                print line
                print ' '
                sleep(1)

    #Metodo para hacer una traza a un host
    def traceme(self, host):
        tracer = Matrix.tracer
        verificacion_traceme = os.popen(tracer + ' ' + host, 'r')
        print verificacion_traceme.read(), "\r\n"
        sleep(1)

    #Metodo para ver un puerto activo con Nmap
    def scanme(self, host, port):
        scanr = Matrix.scanr
        verificacion_scan = os.popen(scanr + ' ' + host + ' -p' + ' ' + str(port))

        #Ciclo FOR para leer la linea 5 que contiene el dato del scan
        i = 0
        for line in verificacion_scan:
            i += 1
            if i == 5:
                print line, "\r\n"
                sleep(1)
                
    #Metodo para revisar informacion Whois
    def whom(self, host):
        idme = Matrix.ider
        print ''
        d = os.popen(idme + ' ' + host + ' | ' + ' tail -n25 ', 'r')

        print ' '
        print d.read()
        print ' '
        sleep(1)

    #Metodo para revisar informacion de records DNS
    def dig(self, host):
        diger = Matrix.diger
        record = str(raw_input('Que record deseas: '))
        print ''
        g = os.popen(diger + ' ' + record.upper() + ' ' + host)
        print g.read()