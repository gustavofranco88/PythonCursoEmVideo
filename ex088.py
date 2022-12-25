# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample, randint
palpites = []
palpite = []
qtn = int(input('Quantos jogos de mega senha deseja? '))
while qtn > 0:
    for i in range(0, 6):
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpites.append(palpite[:])
    palpite.clear()

    qtn -= 1

print(palpites)

