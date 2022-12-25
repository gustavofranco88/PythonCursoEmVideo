# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
pessoas = []
mulheres = []
somaidade = 0
while True:
    pessoa['nome'] = str(input('Qual o nome? '))
    pessoa['sexo'] = str(input('Qual o sexo? (M/F) '))
    pessoa['idade'] = int(input('Qual a idade? '))
    pessoas.append(pessoa.copy())
    somaidade += pessoa['idade']
    op = str(input('Depseja cadastrar mais alguem?(s/n) '))
    if op in 'n/N':
        break

print(pessoas)
print('='*30)
print(f'Total de pessoas cadastradas {len(pessoas)}')
print('='*30)
print(f'Média de idade dos cadastrados {(somaidade / len(pessoas)):.2f} anos ')
print('='*30)
for i in pessoas:
    if i['sexo'] in 'F/f':
        mulheres.append(i['nome'])
if len(mulheres) > 0:
    print(f' A(s) mulher(es) cadastradas ')
    for m in mulheres:
        print(m)
else:
    print('Nenhuma mulher cadastrada')
print('='*30)
print('Pessoa(s) com idade acima da média ')
for p in pessoas:
    if p['idade'] > (somaidade / len(pessoas)):
        for k, v in p.items():
            print(f'{k} = {v}', end='')

