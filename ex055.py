
maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('Digite o peso:  '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso

print(f'O maior peso informado foi {maior}')
print(f'O menor peso informado foi {menor}')

