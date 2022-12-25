temp = []
principal = []
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome ')))
    temp.append(float(input('Digite o peso ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    op = str(input('Deseja continuar? (s/n)'))
    if op in 'n/N':
        break

print(f'Pessoas cadastradas = {len(principal)}')
for p in principal:
    if p[1] == menor:
        print(f'Menor peso = {menor}.kg, Peso de [{p[0]}] ')

for p in principal:
    if p[1] == maior:
        print(f'Maior peso = {maior}.kg, Peso de [{p[0]}] ')

