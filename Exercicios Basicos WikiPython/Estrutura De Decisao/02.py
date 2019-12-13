  #Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um valor positivo ou negativo: '))

if valor > 0:

  print('O valor ', valor, ' é positivo.')

elif valor == 0:

  print('O valor é ', valor)  

else:

  print('O valor ', valor, ' é negativo.')