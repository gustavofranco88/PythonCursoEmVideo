# Exercício Python 097:
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

#programa principal

escreva('Gustavo e Luanna')
