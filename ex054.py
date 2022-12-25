from datetime import date
menor = 0
maior = 0
for i in range(1,8):
    ano = int(input('Digite o ano de nascimento'))
    atual = date.today().year
    idade = atual - ano
    if idade <= 21:
        menor += 1
    else:
        maior += 1
print(f'{menor} são menores')
print(f'{maior} são maiores')


