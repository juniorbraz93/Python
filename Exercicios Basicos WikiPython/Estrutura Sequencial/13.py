# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes 
# fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite o seu peso: '))

h = ( 72.7 * altura ) - 58

m = ( 62.1 * altura ) - 44.7

print('Para homens o peso ideal é: ', h)
print('Para mulheres o peso ideal é: ', m)