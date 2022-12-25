# preencher uma tupla com 5 numeros aleatórios e
# verificar qual é o maior e o menor

from random import randint

tupla = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print(tupla)
maior = 0
menor = 0
i = 0
for num in tupla:
    i += 1
    if i == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    else:
        continue
print(f'menor valor é {menor} e maior valor é {maior}')

# outra maneira
tupla2 = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print(tupla2)
print(max(tupla2))
print(min(tupla2))