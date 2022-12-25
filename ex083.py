#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite uma expressão com parenteses "))
pilha = []
for carater in expressao:
    if carater == '(':
        pilha.append(carater)
    elif carater == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(carater)
            break
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')


