import httplib

class FetchMe:
    def findip(self):
        sitio = 'www.whatismyip.org'
        conn = httplib.HTTPConnection(sitio)
        conn.request('GET', '')
        r1 =  conn.getresponse()
        print 'La ip publica es: ' + ' ' + r1.read()

#    def blacklist(self, host):
#        mxtoolbox = 'www.mxtoolbox.com'
#        verifica = mxtoolbox
#        conn = httplib.HTTPConnection(verifica)
#        conn.request('GET', '/SuperTool.aspx?action=blacklist' + '/\%3a' + host)
#        r2 = conn.getresponse()
#        print r2.read()
