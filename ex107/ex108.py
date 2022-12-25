# Exercício Python 108:
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
import moeda

p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar 10% de  {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p))}')
