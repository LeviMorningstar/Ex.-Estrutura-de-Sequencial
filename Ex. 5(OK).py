print('Esse programa Converte metros para centimetros')
print()
valid_numero = False

while valid_numero == False:
    print()
    m = (input('Digite quantos metros serão convertidos: '))
    print()
    try:
        m = float(m)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)

c = m * 100
print()
print('{} metros é igual a {} centimetros.'.format(m, c))


valid_numero = False
print()
input('Aperte enter para sair')