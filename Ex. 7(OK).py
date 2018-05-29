print('Esse programa calcula a area do quadrado e mostra tambem o seu dobro.')
print()

valid_numero = False

while valid_numero == False:
    n = (input('Digite o valor de um dos lados do quadrado: '))
    try:
        n = float(n)
        valid_numero = True
    except:
        print('Erro na entrada de dados, por favor ultilize somente numeros.')


a = n ** 2
d = a * 2
print()
print('O valor da area é igual a {}m²'. format(a))
print('O Seu Valor dobrado é Igual a {}m²'.format(d))

valid_numero = False

print()
input('Aperte enter para sair')
