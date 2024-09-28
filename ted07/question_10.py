'''Contexto: Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. 
Utilize um loop para realizar os lançamentos e exibir os resultados.'''
import random
def dice_roll():
    dice = random.randint(1,6)
    print(dice)

if __name__ == '__main__':
    print('starting program...')
    play = 0
    while play != 1:
        dice_roll()
        play =int(input('Wanna roll the die again?   \n (press 1 to finish): '))
    print('finishing program...')