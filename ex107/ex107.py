# Exercício Python 107:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(),diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

valor = float(input('Digite o valor R$: '))
aumenta = moeda.aumentar(valor)
diminui = moeda.diminuir(valor)
dobra = moeda.dobro(valor)
metade = moeda.metade(valor)
print(f'{valor} + 10% = {aumenta}')
print(f'{valor} - 10% = {diminui}')
print(f'O dobro de {valor} = {dobra}')
print(f'A metade de {valor} = {metade}')
