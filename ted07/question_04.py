'''Contexto: Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. 
Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.'''

import random
win_condition = int(random.randint(0, 100))
def game(number):
    if number == win_condition:
        print('Congratulations! You won.')
    elif number > win_condition:
        print('Try again! Your number is greater than correct number!')
    elif number < win_condition:
        print('Try again! Your number is less than correct number!')
    else:
        print('not a number')


if __name__ == '__main__':
    print('starting program...')
    numero = int(input('Try to find the correct number!   Type a number to check if yours match the right one:  '))
    game(numero)
    while numero != win_condition:
        numero = int(input('Try to find the correct number!   Type a number to check if yours match the right one:  '))
        game(numero)
    print('finishing program...')