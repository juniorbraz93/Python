# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# * A mensagem "Reprovado", se a média for menor do que sete;
# * A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a  1º Nota: '))
nota2 = float(input('Digite a  2º Nota: '))
nota3 = float(input('Digite a  3º Nota: '))
nota4 = float(input('Digite a  4º Nota: '))


media = (nota1 + nota2 + nota3 + nota4) / 4


print('Sua média e de: ', media)

if media > 7 and media < 9:

  print('Aprovado')

elif media == 10:

  print('Aprovado com Distinção')

else:

  print('Reprovado')