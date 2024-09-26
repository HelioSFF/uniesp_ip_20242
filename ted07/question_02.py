'''Contexto: Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse 
número (de 1 a 10). Utilize um loop para realizar as multiplicações e exibir os resultados de 
forma organizada. '''

def tabuada(number):
    for i in range(1,11):
        print(f'{number} multiplicado por {i} é igual a {number * i}')

if __name__ == '__main__':
    print('starting program...')
    tabuada(3)
    print('finishing program...')