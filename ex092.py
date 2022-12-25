# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome '))
trabalhador['anoNascimento'] = int(input('Ano de Nascimento '))
trabalhador['CTPS'] = int(input('Carteira de Trabalho (se não tem, digite 0) '))
trabalhador['idade'] = datetime.now().year - trabalhador['anoNascimento']
if trabalhador['CTPS'] == 0:
    print('sem carteira')
else:
    trabalhador['salario'] = float(input('Digite o salario '))
    trabalhador['anoContratação'] = int(input('Ano de contratação '))
    trabalhador['aposenta'] = trabalhador['idade'] + ((trabalhador['anoContratação'] + 40) - datetime.now().year)

print('*'*30)
print(f'nome = {trabalhador["nome"]}')
print(trabalhador['idade'])
print(trabalhador['salario'])
print(trabalhador['anoContratação'])
print(f' vai se aposentar com {trabalhador["aposenta"]} anos')
