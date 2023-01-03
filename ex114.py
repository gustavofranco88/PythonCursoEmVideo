import urllib
import urllib.request


def checkConecttion(url):
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        return 'Sem conexão'

    else:
        return 'Conectado'

teste = checkConecttion("http://www.google.com")
print(teste)
