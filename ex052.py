#numeros primos

num = int(input('Digite um numero inteiro,\npra verificar se ele é primo '))

for i in range(2, num+1):
    if (num % i == 0) and i < num:

        print(f'O resto da divisão de {num} por {i} = {num % i}')
        print(f'o numero {num} não é primo')
        break
    else:
        if i < num:
            continue
        else:
            print(f'{num} é primo')



