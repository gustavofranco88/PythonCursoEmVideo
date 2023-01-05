# ex115-1.py
def leiaInt(texto):
    #print(linha())
    while True:
        try:
            num = int(input(texto))
        except (TypeError, ValueError):
            print('\033[0;31mErro, digite uma das opções acima\033[m')
            leiaInt('Sua opção: ')
        except KeyboardInterrupt:
            print('Interrompido pelo usuario')
            break
        else:
            return num


def linha(tam=42):
    return '-'*tam

def cabecalho(tex):
    print(linha())
    print(tex.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU DE CADASTRO')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m-\033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('Sua opção: ')
    print(linha())
    return opc



