print('Este programa Calcula seu salario com base no Valor a hora.')
print()

valid_v = False
valid_h = False

while valid_v == False:
    v = (input('Digite o valor da sua hora: '))
    try:
        v = float(v)
        valid_v = True
    except:
        print('Erro na entrada de dados.')

while valid_h == False:
    h = int(input('Digite quantas horas você trabalha no mês: '))
    try:
        h = int(h)
        valid_h = True
    except:
        print('Erro na entrada de dados.')


print()
print('No final do mês você vai ganhar {:.2f}'.format(v * h))
print()

valid_v = False
valid_h = False
input('Aperte enter para sair')