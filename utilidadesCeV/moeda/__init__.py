# funçoes

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + preço * (taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - preço * (taxa / 100)
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(m=0.0, moeda='R$'):
    return f'{moeda}{m:.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, desconto=0):
    print('-' * 30)
    print('  RESUMO DO VALOR  '.center(30))
    print('-' * 30)
    print(f'  Preço analisado: \t{moeda(preço)}')
    print(f'  Dobro do preço: \t{dobro(preço, True)}') # \t serve para tabular o item
    print(f'  Metade do preço: \t{metade(preço, True)}')
    print(f'  Aumento de {aumento}%: \t{aumentar(preço, aumento, True)}')
    print(f'  Desconto de {desconto}%: \t{diminuir(preço, desconto, True)}')
    print('-' * 30)
