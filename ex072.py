
lanches = 'Hamburger', 'hot dog', 'suco', 'café'

for count in range(0, len(lanches)):
    print(count)
   # print(lanches(count))

for lanche in lanches:
    print(lanche)

for pos,lanche in enumerate(lanches):

    print(f'O {lanche} está na posição {pos}')

