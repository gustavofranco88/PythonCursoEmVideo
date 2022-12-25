# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

total = 0
jogador = dict()
gols = []

jogador['nome'] = str(input('Qual o  nome do jogador? '))
jogador['partidas'] = int(input(f'Quantos partidas fez {jogador["nome"]}? '))
if jogador['partidas'] > 0:
    for i in range(1, jogador['partidas']+1):
        gols.append(int(input(f' Quantos gols {jogador["nome"]} fez na partida {i}? ')))

jogador['gols'] = gols[:]
jogador['totalgoals'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} é {v} ')
print('-='*30)
print(f'{jogador["nome"]} fez {jogador["totalgoals"]}')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i} fez {g}')
print('-='*30)
