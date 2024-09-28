'''Contexto: Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. 
Utilize um loop para realizar as multiplicações necessárias.'''

def factorial(number):
    fac = 1
    for i in range(1,number+1):
        fac *= i
    print(f'factorial is equal {fac}')

if __name__ == '__main__':
    print('starting program...')
    factorial(5)
    print('finishing program...')


