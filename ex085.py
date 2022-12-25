# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = []
pares = []
impares = []

for i in range(0, 7):
    num = int(input('Digite um numero '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

numeros.append(sorted(pares))
numeros.append(sorted(impares))
print(numeros)
