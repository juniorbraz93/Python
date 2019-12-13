salario = float(input('Informe o valor do seu salário: '))
print('')
despesa = float(input('Qual o valor de suas despesas? '))
print('')

receita = salario - despesa
calculo = receita * 12
anos = 1000000 / calculo

print('Economizando',receita, 'por mês, você poupará ')
print("R$ 1.000.000,00 em",anos," anos.")