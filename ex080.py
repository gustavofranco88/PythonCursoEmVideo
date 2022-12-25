# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
for i in range(0, 5):
    valor = int(input('Digite um valor '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
       #print('Adicionado com sucesso')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                break
            pos += 1

print('-' * 20)

print(valores)
