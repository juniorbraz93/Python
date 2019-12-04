# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
#
# Obs.: Salário Bruto - Descontos = Salário Líquido.

horas = int(input('Qunatas horas você trabalha por mês:'))
porHora = float(input('Quanto você ganha por hora: '))

salarioBruto = porHora * horas
ir =  salarioBruto * 0.89 
desc1 = salarioBruto - ir
inss = salarioBruto * 0.92
desc2 = salarioBruto - inss
sind = salarioBruto * 0.95
desc3 = salarioBruto - sind

salarioLiq = salarioBruto - desc1 - desc2 - desc3

print('+ Salário Bruto : R$', salarioBruto)
print('- IR (11%) : R$', desc1)
print('- INSS (8%) : R$', desc2)
print('- Sindicato ( 5%)', desc3)
print('= Salário Liquido : R$', salarioLiq)
