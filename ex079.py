# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:
    valor = int(input('Digite um valor '))
    if valor not in valores:
        valores.append(valor)
        print('Adicionado com sucesso')
    else:
        print('Valor duplicado, não adicionado')
    resposta = str(input('Deseja continuar? S/N '))
    if resposta in 'Nn':
        break
print('--' * len(valores))
valores.sort()
print(valores)
