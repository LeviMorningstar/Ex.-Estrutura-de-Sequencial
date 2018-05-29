print('Inicio do Programa')
print()

valid_n1 = False
valid_n2 = False
valid_r1 = False

while valid_n1 == False:
    n1 = (input('Digite um número inteiro: '))
    try:
        n1 = int(n1)
        valid_n1 = True
    except:
        print('Erro, Valor invalido.')

while valid_n2 == False:
    n2 = (input('Digite um outro numero inteiro: '))
    try:
        n2 = int(n2)
        valid_n2 = True
    except:
        print('Erro, Valor invalido.')

while valid_r1 == False:
    r1 = float(input('Digite um numero real: '))
    try:
        r1 = float(r1)
        valid_r1 = True
    except:
        print('Erro, Ultilize somente numeros e use pontos nos lugares das Virgulas.')

a = (n1*2) + (n2/2)
b = (n1*3) +r1
c = r1**3



print()
print('A soma do dobro de {} com metade de {} é {}.'.format(n1, n2, a))
print('A soma do triplo de {} com {:.2f} é {:.2f}.'.format(n1, r1, b))
print('{:.2f} elevado ao cubo é {:.2f}.'.format(r1, c))

valid_n1 = False
valid_n2 = False
valid_r1 = False


print()
input('Aperte enter para sair')