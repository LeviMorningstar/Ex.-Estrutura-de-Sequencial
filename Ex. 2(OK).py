print('Este Programa mostra o numero informado.')
print()

valid_input = False

while valid_input == False:
    n = (input('Digite o Número: '))
    try:
        n = int(n)
        valid_input = True
    except:
        print('===' *15)
        print('Erro, por favor Digite apenas numeros.')
        print('===' *15)

print()
print('O número informado foi {}'.format(n))

valid_input = False
print()
input('Aperte enter para sair')