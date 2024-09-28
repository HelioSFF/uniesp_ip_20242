'''Contexto: Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. 
Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.'''

def dectobin(number):
    bina = ''
    if number == 0:
        return '0'
    while number > 0:
        bina += str(number%2)
        number = number//2
    print(bina[::-1])
if __name__ == '__main__':
    print('starting program...')
    dectobin(55)
    print('finishing program...')