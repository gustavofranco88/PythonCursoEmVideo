# funçoes para tratar arquivos
from ex115.lib.interface import *
def arquivoExixte(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'a')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome}, criado com sucesso ')


def lerArquivo(nome):
    try:
        a = open(nome, 'r')
       # a.close()
    except:
        print('Erro ao ler arquivo')
    else:
        for pessoa in a:
            dado = pessoa.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'a')
    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar, tente novamente')
        else:
            print('Cadastrado com sucesso')
'''
#pessoas = open('pessoas.txt', 'r')
        for linha in pessoas:
            pessoa = linha
            print(pessoa)
'''