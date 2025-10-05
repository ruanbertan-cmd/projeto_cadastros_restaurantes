import os
'''
numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    os.system('cls')
    print(f'O número {numero} é par')
else:
    os.system('cls')
    print(f'O número {numero} é impar')
'''

idade = int(input('Digite a sua idade: '))

if 0 < idade <= 12:
    print('Criança')
elif 13 < idade <= 17:
    print('Adolescente')
elif 17 < idade:
    print('Adulto')
else:
    print('Idade inválida')