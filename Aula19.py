pessoas = {'nome': 'Gustavo', 'idade': 34, 'sexo': 'm'}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Dexter'
pessoas['idade'] = 5
pessoas['peso'] = 35
print(pessoas)

# dicionário dentro de listas
estado1 = {'uf':'Bahia', 'sigla':'BH'}
estado2 = {'uf':'Pernambuco', 'sigla':'PE'}
estados = []
estados.append(estado1)
estados.append(estado2)
print(estados)

estado = {}
brasil = []
for i in range(0,3):
    estado['uf'] = str(input('Digite o Estado: '))
    estado['capital'] = str(input('Digite a capital: '))
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
     #   print(f'{k} {v}')
    for v in e.values():
        print(f'{v}', end=' ')

