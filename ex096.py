# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a,b):
    tam = a*b
    print(f'A area do terreno {a}m x {b}m é {tam}m²')

print('-'*50)
print('Area do Terreno')
print('-'*50)
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura, comprimento)



