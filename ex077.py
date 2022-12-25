#analisando as vogais das palavras

palavras = 'tomate', 'televisao', 'sofa', 'python', 'estudar', 'pdc'

for palavra in palavras:
    print(f'\nA palavra {palavra} tem essas vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    