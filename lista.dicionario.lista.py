# acessar uma lista dentro de um dicionario que está dentro uma lista

time = [{'nome': 'Manga', 'partidas': 3, 'gols': [1, 2, 1], 'totalgoals': 4},
           {'nome': 'Gamalho', 'partidas': 3, 'gols': [2, 2, 1], 'totalgoals': 5}]
#acessando so dicionarios
mostrar = int(input('Mostrar dados de qual jogador?(Cod.) ou (999 para sair) '))
print(f'{time[mostrar]["nome"]}')# mostra o nome do jogador escolhido
# acessando a lista dentro do dicionário
for i, g in enumerate(time[mostrar]['gols']):
    print(f'Na partida {i+1} fez {g} gol(s)')
#print(f'{time[mostrar]["nome"]}')# mostra o nome do jogador escolhido
