# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno '))
aluno['media'] = float(input('Digite a média do aluno '))

if aluno['media'] >= 7:
    situacao = 'aprovado'
    aluno['situacao'] = situacao
elif aluno['media'] >= 4:
    situacao = 'em recuperação'
    aluno['situacao'] = situacao
else:
    situacao = 'reprovado'
    aluno['situacao'] = situacao

print(f'o Aluno {aluno["nome"]} teve média {aluno["media"]} e está {aluno["situacao"]}')
