# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#     A) A soma de todos os valores pares digitados.
#     B) A soma dos valores da terceira coluna.
#     C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacol = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]= '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacol += matriz[l][c]
        if l == 1:
            if maior < matriz[l][c]:
                maior = matriz[l][c]


print('-='*20)
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[li][c]:^5}]', end='')
    print()
print(f'Soma dos pares da matriz {somapar}')
print(f'Soma da terceira coluna {somacol}')
print(f'Maior valor da sedgunda coluna {maior}')

