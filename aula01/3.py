palavra = str(input('insira a palavra aqui: '))

letra=str(input('o que vc procura?: '))

print('=================')

contador=1
for aux in palavra:
    if letra == aux:    
        print(str(contador),end='/ ')
    contador+=1   