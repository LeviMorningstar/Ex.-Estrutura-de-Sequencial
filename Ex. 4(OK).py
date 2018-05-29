print('Esse programa faz a média entre 4 notas Bimestrais:')
print()

valid_numero = False

while valid_numero == False:
    print()
    n1 = input('Digite a Primeira nota: ')
    print()
    try:
        n1 = int(n1)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)

valid_numero = False

while valid_numero == False:
    print()
    n2 = (input('Digite a segunda nota:'))
    print()
    try:
        n2 = int(n2)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

valid_numero = False
while valid_numero == False:
    print()
    n3 = input('Digite terceira nota: ')
    print()
    try:
        n3 = int(n3)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)

valid_numero = False

while valid_numero == False:
    print()
    n4 = (input('Digite a quarta nota:'))
    print()
    try:
        n4 = int(n4)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

media = (n1+n2+n3+n4) /4

print()
print('A media das notas é {:.2f}'.format(media))

print()
input('Aperte enter para sair')