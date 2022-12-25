# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda

p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentar 10% de  {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}')
print(f'Diminuir 10% de  {moeda.moeda(p)} é {moeda.diminuir(p, 10, True)}')
