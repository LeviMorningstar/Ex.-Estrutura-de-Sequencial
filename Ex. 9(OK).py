print('==='*20)
print('    Esse programa converte C° para F° e vice e versa.')
print('==='*20)
print()

lista = ['c', 'f']

valid_escolha = False

while valid_escolha == False:
    escolha = input("Digite 'c' para C° ou 'f' para Fº:").lower()
    print()
    if escolha not in lista:
        print('Valor invalido, por favor digite somente umas das opções informadas.')
        print()
    else:
        valid_escolha = True


if escolha == 'c':
    c = float(input('Digite o valor em Cº: '))
    f = (c * 1.8) + 32
    print('O valor {:.2f}C° é igual a {:.2f}Fº.'. format(c, f))

elif escolha == 'f':
    fair = float(input('Digite o calor em Fº: '))
    cels = (5 * (fair-32)) / 9
    print('O valor {:.2f}F° é igual a {:.2f}Cº.'.format(fair, cels))

else:
    print('Valor Não reconhecido.')

valid_escolha = False

print()
input('Aperte enter para sair')