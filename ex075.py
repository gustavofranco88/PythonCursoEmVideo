# Leia quatro numeros do teclado e guarde em uma tupla.
# Mostre quantaz vezes apareceu o num 9, em que posição foi digitado o primeiro 3
# e quais são pares

numeros = (int(input('Primeiro numero ')),
           int(input('Primeiro numero ')),
           int(input('Primeiro numero ')),
           int(input('Primeiro numero ')))

print(numeros)
print(f'O nove apareceu {numeros.count(9)} vezes')
print(f'O primeiro três está na posição {numeros.index(3)+1}')

for num in numeros:
    if num % 2 == 0:
        print(f'os pares são {num} ', end=' ')

print((numeros))