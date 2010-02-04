"""
Con esta clase le pedimos al usuario que agrege el servidor
a verificar
"""


class Hostme():
    def __init__ (self, host):
        while len(host) <= 0:
            host = raw_input('Dame el host o ip: ')
            self.host = host.lstrip('htp:/')
