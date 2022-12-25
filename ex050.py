from random import random, randint, sample

aleatorios = sample(range(100), 10)
aleatorios2 = aleatorios[:]
soma = 0
c = 0
for numero in aleatorios:
   if numero % 2 == 0:
    soma += numero
    aleatorios2.append(soma)
    c += 1

print(aleatorios)
print(aleatorios2)
print(soma)
print(c)
