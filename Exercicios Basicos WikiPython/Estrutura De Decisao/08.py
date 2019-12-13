# Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

Nprodut1 = input('O nome do primeiro produto: ')
produt1 = float(input('O preço do primeiro produto: '))
Nprodut2 = input('O nome do segundo produto: ')
produt2 = float(input('O preço do segundo produto: '))
Nprodut3 = input('O nome do terceiro produto: ')
produt3 = float(input('O preço do terceiro produto: '))


if produt1 < produt2 and produt1 < produt3:

  print('O produto ', Nprodut1, ' com o preço R$ ', produt1)

elif produt2 < produt1 and produt2 < produt3:

  print('O produto ', Nprodut2, ' com o preço R$ ', produt2)

elif produt3 < produt1 and produt3 < produt2:

  print('O produto ', Nprodut3, ' com o preço R$ ', produt3)

else:

  print('Erro')

