# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto():
    ano_nascimento = int(input('Que ano vc nasceu? '))
    idade = datetime.now().year - ano_nascimento
    if idade <= 15:
        print(f'{idade} anos')
        votar = input('Você não tem idade para votar')
    elif idade >= 18 and idade <= 65:
        print(f'{idade} anos')
        votar = input('Seu voto é OBRIGATÓRIO')
    else:
        print(f'{idade} anos')
        votar = input('Seu voto é OPCIONAL')
    return votar


eleição = voto()

