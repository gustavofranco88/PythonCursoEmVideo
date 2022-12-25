# Exercício Python 103:
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(gols, nome = 'Desconhecido'):
    print(f'O jogador {nome.title()} fez {gols} gols')

n = str(input('Qual o nome do jogador? '))
g = str(input('Quantos gols ele fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(g)
else:
    ficha(g, n)


