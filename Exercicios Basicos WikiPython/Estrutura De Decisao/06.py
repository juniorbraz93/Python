#Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input('Digite primeiro numero? '))
num2 = int(input('Digite segundo numero? '))
num3 = int(input('Digite terceiro numero? '))

if num1 > num2 and num1 > num3:

  print('O número ', num1, ' é o maior que ', num2, num3)

elif num2 > num1 and num2 > num3:

  print('O número ', num2, ' é o maior que ', num1, num3)

else:

  print('O número ', num3, ' é o maior que ', num2, num1)
  
