print('-' * 14)
print('Menu de Opções')
print('-' * 14)
print()
print('1. Média Aritmética')
print('2. Média Ponderada')
print('3. sair')
print()
menu = input('Digite a sua opção desejada: ')
print()
cont = 1
media = 0

if menu == '1':

    print('-' * 18)
    print(' Média Aritmética ')
    print('-' * 18)
    print()

    ma = int(input('Digite a contidade de valores que deseja: '))

       while (cont < ma):
            n = int(input("Digite o", cont, "º valor: "))
            cont = cont + 1
            media = media + n
        else:
            pass
mediaf = media / ma

elif menu == '2':

    print('-' * 17)
    print(' Média Ponderada ')
    print('-' * 17)
    print()

    nota1 = float(input('Digite a  1º Nota: '))
    nota2 = float(input('Digite a  2º Nota: '))
    nota3 = float(input('Digite a  3º Nota: '))

    mediaf = (nota1 * 4 + nota2 * 4 + nota3 * 2) / 10

    if mediaf >= 5:
        print('Aprovado')
    else:
        print('Reprovado')

    print('A Média Ponderada: ', mediaf)

elif menu = '3':
  print('Fim do Programa')

else:

  print('ERRO')
