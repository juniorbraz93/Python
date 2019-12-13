# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2
# questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
# como "Inocente".

clas = 0
print('Responda S - Sim e N - Não')
resp1 = input('Telefonou para a vítima? ')

resp1 = resp1.upper()

if resp1 == 'S':
    clas = clas + 1

resp2 = input('Esteve no local do crime? ')

resp2 = resp2.upper()

if resp2 == 'S':
    clas = clas + 1

resp3 = input('Mora perto da vítima? ')

resp3 = resp3.upper()

if resp3 == 'S':
    clas = clas + 1

resp4 = input('Devia para a vítima? ')

resp4 = resp4.upper()

if resp4 == 'S':
    clas = clas + 1

resp5 = input('Já trabalhou com a vítima? ')

resp5 = resp5.upper()

if resp5 == 'S':
    clas = clas + 1

print(clas)
print('Sua Classificação  sobre a participação da pessoa no crime')
print()

if clas == 0 or clas == 1:
    print('Inocente')
elif clas == 2:
    print('Suspeita')
elif clas == 3 or clas == 4:
    print('Cúmplice')
elif clas == 5:
    print('Assassino')
else:
    print('ERRO')
