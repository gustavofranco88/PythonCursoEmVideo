#FAça u  programa q calcule a soma de todos os multiplos de 3
#em um intervalo de 1 à 500
s = 0
cont = 0
for i in range(1,501):
    if i % 2 == 0:
        continue
    else:
        if i % 3 == 0:
            print(f'{i}', end=' ')
            s += i
            cont += 1
print('\n')
print(f'soma dos {cont} numeros, que são multiplos de 3, é {s}')

