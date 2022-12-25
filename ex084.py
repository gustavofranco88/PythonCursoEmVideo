# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
count = 0
menor = 0
maior = 0
maiorp = []
menorp = []
nomes = []
pesos = []

while True:
    pessoas.append(str(input('Digite o nome ')))
    pessoas.append(int(input('Digite o peso ')))
    op = str(input('Deseja continuar? (s/n)'))
    if op in 'n/N':
        break

for i, p in enumerate(pessoas):
    if type(p) == str:
        count += 1
    elif p >= maior:
        maior = p
    else:
        menor = p

for i, m in enumerate(pessoas):
    if type(m) != str:
        if m == maior:
            maiorp.append(i - 1)
        else:
            menorp.append(m - 1)
    else:
        continue

print(f'Pessoas cadastradas = {count}')
print(f'Menor peso = {menor}.kg, Peso de {menorp}')
print(f'Maior peso = {maior}.kg, Peso de {maiorp}')
***
# PROFESSOR


