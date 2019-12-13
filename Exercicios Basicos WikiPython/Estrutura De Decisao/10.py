#Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite o que turno você estuda M-matutino ou V-Vespertino ou N- Noturno: ')

turno = turno.lower()

if turno == 'm':

  print('Você estuda no turno matutino, Bom Dia!')

elif turno == 'v':

  print('Você estuda no turno vespertino, Boa Tarde!')

elif turno == 'n':

  print('Você estuda no turno noturno, Boa Noite!')

else:

  print('Valor Inválido!')
