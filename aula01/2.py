a=str(input('insira o valor de a:'))
b=str(input('insira o valor de b:'))
if len(a)< len(b):
    print ('Não deu')
else:
    a=a[-len(b):] 


if (a) == (b):
    print('Encaixa')
else:
    print('Não encaixa')