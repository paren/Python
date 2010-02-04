class Portme():
    def __init__ (self, port):
        while len(port) <= 0:
            port = raw_input('Dame un puerto: ')
            self.port = port


