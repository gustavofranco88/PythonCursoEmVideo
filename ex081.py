#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(float(input('Digite um numero ')))
    res = str(input('Deseja continuar? S/N '))
    if res in 'Nn':
        break
    elif res in 'Ss':
        continue
    else:
        print('opção errada')
    res = str(input('Deseja continuar? S/N '))

print(f'\nVoce digitou {len(numeros)} numeros ')
numeros.reverse()
print(numeros)
if 5 in numeros:
    print('Cinco está na lista ')
else:
    print('Cinco não está na lista')

