# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

F = float(input('Informe a temperatura em ºF: '))

C = (5 * (F-32) / 9)

C = int(C)

print('A temperatura informada em ', F, ' ºF é em ', C,'ºC.')