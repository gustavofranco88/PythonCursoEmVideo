from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

pessoas = 'pessoas.txt'
if not arquivoExixte(pessoas):
    criarArquivo(pessoas)

while True:
    reposta = menu(['Cadastrar usuario', 'Lista de usuarios', 'Sair do sistema'])
    if reposta == 1:
        cabecalho('Cadastrar Usuario')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(pessoas, nome, idade)

    elif reposta == 2:
        cabecalho('Usuarios')
        lerArquivo(pessoas)

    elif reposta == 3:
        cabecalho('Volte sempre')
        break
    else:
        cabecalho('\033[31mErro, digite uma das opções acima\033[m')
    sleep(2)
