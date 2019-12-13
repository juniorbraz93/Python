#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input('Digite primeiro numero? '))
num2 = int(input('Digite segundo numero? '))
num3 = int(input('Digite terceiro numero? '))

if num1 > num2 and num2 < num3:

  print('O maior número é', num1, ' é o menor número é: ', num2)

elif num1 > num3 and num3 < num2:

  print('O maior número é', num1, ' é o menor número é: ', num3)

elif num2 > num1 and num1 < num3:

  print('O maior número é', num2, ' é o menor número é: ', num1)

elif num2 > num3 and num3 < num1:

  print('O maior número é', num2, ' é o menor número é: ', num3)

elif num3 > num2 and num2 < num1:

  print('O maior número é', num3, ' é o menor número é: ', num2)

elif num3 > num1 and num1 < num2:

  print('O maior número é', num3, ' é o menor número é: ', num1)

else:

  print('Erro')