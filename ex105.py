# Exercício Python 105:
# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# a)  – Quantidade de notas
# b)– A maior nota
# c)– A menor nota
# d)– A média da turma
# e)– A situação (opcional)

def notas(*nota, sit = False):
    infoaluno = {}
    infoaluno['total'] = len(nota)
    infoaluno['maior'] = max(nota)
    infoaluno['menor'] = min(nota)
    infoaluno['media'] = sum(nota) / len(nota)
    if infoaluno['media'] < 4:
        situ = 'RUIM'
    elif infoaluno['media'] < 7:
        situ = 'RASOÁVEL'
    else:
        if infoaluno['media'] < 8:
            situ = 'BOA'
        else:
            situ = 'ÓTIMA'
    infoaluno['Situação'] = situ
    print(infoaluno)


notas(8, 9, 3, 4)


