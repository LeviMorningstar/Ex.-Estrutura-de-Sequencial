print('Esse Programa soma dois números')
print()

valid_numero = False
while valid_numero == False:
    print()
    n1 = input('Digite o Primeiro número: ')
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
    n2 = (input('Digite outro número:'))
    print()
    try:
        n2 = int(n2)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

soma = n1 + n2

valid_numero = False
print()
print('A soma entre {:.2f} e {:.2f} é igual á {:.2f}'.format(n1, n2, soma))

print()
input('Aperte enter para sair')