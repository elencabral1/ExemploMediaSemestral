'''
Escreva um programa em Python que leia 3 notas, calcule e imprima a média, e o conceito de acordo com a tabela abaixo:
- média maior ou igual a 9 - Conceito A
- média maior do que 8 e menor 8.9 - Conceito B 
- média maior do que 7 e menor 7.9 - Conceito C
- média maior do que 6 e menor 6.9 - Conceito D
- média maior do que 6 - Conceito E
Utilize as estruturas condicionais (if-elif-else e match-case), para encontrar a média e imprimir o conceito
'''

print('Média semestral')

nota1 = float(input('Digite sua nota de JavaScript: '))
nota2 = float(input('Digite sua nota de PHP: '))
nota3 = float(input('Digite sua nota de Java: '))

media = (nota1 + nota2 + nota3)/3


if media >=9:
    conceito = 'A'
elif media >=8 and media <=8.9:
    conceito = 'B'
elif media >=7 and media <=7.9:
    conceito = 'C'
elif media >=6 and media <=6.9:
    conceito = 'D'
else:
    conceito = 'E'

match conceito:
    case 'A':
        print('Média foi: ', media)
        print('Conceito', conceito)
    case 'B':
        print('Média foi: ', media)
        print('Conceito', conceito)
    case 'C':
        print('Média foi: ', media)
        print('Conceito', conceito)
    case 'D':
        print('Média foi: ', media)
        print('Conceito', conceito)
    case 'E':
        print('Média foi: ', media)
        print('Conceito', conceito)
    
              
        
              
