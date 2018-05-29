print('Esse programa calcula a Area do circulo:')
print()

valid_numero = False

while valid_numero == False:
    print()
    r = (input('Digite o valor do Raio: '))
    print()
    try:
        r = float(r)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)


a = 3.1415 * (r ** 2)

print()
print('O valor da area é igual á {:.2f}'. format(a))

valid_numero = False

print()
input('Aperte enter para sair')