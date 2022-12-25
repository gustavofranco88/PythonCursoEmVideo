# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
for p in range(0, 5):
    numeros.append(int(input(f'Digite um numero para a posição {p} ')))
print(f'O maior valor foi {max(numeros)} e esta na posição ')

for p, num in enumerate(numeros):
    if num == max(numeros):
        print(p,  end=' ')

# print(f'O maior valor é {max(numeros)} e esta na posição: ',end=' ')
# print(f'O menor valor é {min(numeros)} e esta na posição: ',end=' ')
