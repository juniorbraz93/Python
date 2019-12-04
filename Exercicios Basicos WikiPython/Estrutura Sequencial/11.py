# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
n3 = int(input('Digite o 3º numero: '))

dobro = n1 * 2
triplo = n2 * 3
cubo = n3 ** 2

print('O dobro do ', n1,' é ', dobro)
print('O triplo do ', n2,' é ', triplo)
print('O cubo do ', n3,' é ', cubo)
