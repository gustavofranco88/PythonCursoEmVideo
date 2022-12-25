# funçoes

def mostraLinha(): # mostrar varias linhas na tela
    print('-'*30)
def topo(msg): # mensagem para titulos
    print('-' * 30)
    print(msg)
    print('-' * 30)
def soma(a, b): #função com parametros definidos
    soma = a + b
    print(soma)

def multi(* num):
    print(len(num))
    soma = 0
    for i in num:
        soma += i
    print(soma)




mostraLinha()
print('FUNÇÕES')
mostraLinha()
topo('   GUSTAVO    ')
soma(2, 1)
multi(1, 3, 7, 8, 9, 3)

