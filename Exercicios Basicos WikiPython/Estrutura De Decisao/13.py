#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor 
# inválido.

print('(1- Domingo, 2- Segunda, 3- Terça, 4- Quarta, 5- Quinta, 6- Sexta, 7- Sabado.)')
dia = input('Digite um número e exiba o dia correspondente da semana: ')

if dia == '1':

  print('Domingo')

elif dia == '2':

  print('Segunda')

elif dia == '3':

  print('Terça')

elif dia == '4':

  print('Quarta')

elif dia == '5':

  print('Quinta')

elif dia == '6':

  print('Sexta')

elif dia == '7':

  print('Sabado')

else:

  print('valor inválido!')