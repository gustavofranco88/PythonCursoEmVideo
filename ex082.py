# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um número ')))

    op = str(input('Deseja continuar S/N '))
    if op in 'n/N':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        # if i not in pares:
        pares.append(v)
    else:
    # if i not in impares:
        impares.append(v)

print('-' * 30)
print(f'Lista de numeros {numeros} ')
print('-' * 30)
print(f'Lista de numeros pares{pares} ')
print('-' * 30)
print(f'Lista de numeros impares{impares}')
print('-' * 30)
