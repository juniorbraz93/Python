# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

 # 1L = 3m
 # 18L = R$ 80

metros = int(input('Quantos metros quadrados da área a ser pintada: '))

latas = metros / 18
ptotal = latas * 80


print('A quantidade de latas de tintas são: ', latas)
print('O preço total da compra e de: R$',ptotal)
s