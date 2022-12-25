# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

total = 0
jogador = dict()
time = []
gol = []

while True:
    jogador['nome'] = str(input('Qual o  nome do jogador? '))
    jogador['partidas'] = int(input(f'Quantos partidas fez {jogador["nome"]}? '))
    if jogador['partidas'] > 0:
        for i in range(1, jogador['partidas']+1):
            gol.append(int(input(f' Quantos gols {jogador["nome"]} fez na partida {i}? ')))

    jogador['gols'] = gol[:]
    jogador['totalgoals'] = sum(gol)
    time.append(jogador.copy())
    jogador.clear()
    gol.clear()
    cad = str(input('Adicionar outro jogador? (s/n) '))
    if cad in 'n/N':
        break
print(time)
print('-='*30)
print(f'{"Cod.":<4} {"Nome":^10} {"Partidas":^10} {"Gols":^3}')
for i, j in enumerate(time):
    print(f'{i:<4} {j["nome"]:^10} {j["partidas"]:^10} {j["totalgoals"]:^3} ')
# print(j)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} é {v} ')
print('-='*30)
while True:
    mostrar = int(input('Mostrar dados de qual jogador?(Cod.) ou (999 para sair) '))
    if mostrar == 999:
        break
    elif mostrar >= len(time):
        print('jogador não existe')
    else:
        print(f'{time[mostrar]["nome"]}')  # mostra o nome do jogador escolhido
        # acessando a lista dentro do dicionário
        for i, g in enumerate(time[mostrar]['gols']):
            print(f'Na partida {i + 1} fez {g} gol(s)')
print('-='*30)

