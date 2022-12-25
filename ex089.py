# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    nome = str(input('Nome '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    op = str(input('Deseja continuar? [S/N] '))
    if op in 'Nn':
        break
print(alunos)
print('=' * 30)
print(f'{"No.":<4}{"nome":<10}{"Média":>5}')

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>5.1f}')
print('*' * 30)
while True:
    opc = int(input('Escolha um aluno para mostrar: [999 para sair]'))
    if opc == 999:
        print('Fim')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')

print('VOLTE SEMPRE')
