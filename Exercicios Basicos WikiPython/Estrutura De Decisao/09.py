#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Digite primeiro numero? '))
num2 = int(input('Digite segundo numero? '))
num3 = int(input('Digite terceiro numero? '))

if num1 < num2 and num1 < num3 and num2 < num3:

  print(num1)
  print(num2)
  print(num3)

elif num1 < num2 and num1 < num3 and num3 < num2:

  print(num1)
  print(num3)
  print(num2)

elif num2 < num1 and num2 < num3 and num1 < num3:

  print(num2)
  print(num1)
  print(num3) 


elif num2 < num1 and num2 < num3 and num3 < num1:

  print(num2)
  print(num3)
  print(num1)

elif num3 < num1 and num3 < num2 and num1 < num2:

  print(num3)
  print(num1)
  print(num2)

elif num3 < num1 and num3 < num2 and num2 < num1:

  print(num3)
  print(num2)
  print(num1)

else:

  print('ERRO')  