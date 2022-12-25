# simular saque caixa eletronico
notas = 50, 20, 10, 5
saque = int(input('Quanto quer sacar: '))
count50 = 0
count20 = 0
count10 = 0
count5 = 0

while saque > 0:
    if saque % 5 == 0:
        if saque >= 50:
            saque -= 50
            count50 += 1
        elif saque >= 20:
            saque -= 20
            count20 += 1
        elif saque >= 10:
            saque -= 10
            count10 += 1
        elif saque >= 5:
            saque -= 5
            count5 += 1
        else:
            print(('Saque realizado'))
            break
    else:
        print(('Saque não realizado, digite um valor valido'))
        saque = int(input('Quanto quer sacar: '))

if saque == 0:
    if count50 > 0:
        print(f'{count50} notas de 50')
    if count20 > 0:
        print(f'{count20} notas de 20')
    if count10 > 0:
        print(f'{count10} notas de 10')
    if count5 > 0:
        print(f' {count5} notas de 5')
