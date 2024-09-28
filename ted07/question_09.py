'''Contexto: Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. 
Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.'''

def draw(option):
    if option == 1:
        draw_triangle(int(input('Please type the height of the triangle: ')))
    elif option == 2:
        draw_square(int(input('Please type the size of the square:  ')))
    elif option == 3:
        draw_diamond(int(input('Please type the size of the diamond: ')))
    else:
        print('Error')
def draw_triangle(height):
    print("Triângulo:")
    for i in range(1, height + 1):
        print('*' * i)
    print('')

def draw_square(size):
    print("Quadrado:\n")
    for i in range(size):
        print('*' * size)
    print('')

def draw_diamond(size):
    if size % 2 == 0:
        size += 1
    print("Losango:\n")
    for i in range(size // 2 + 1):
        print(' ' * (size // 2 - i) + '*' * (2 * i + 1))
    for i in range(size // 2 - 1, -1, -1):
        print(' ' * (size // 2 - i) + '*' * (2 * i + 1))
    print('')


if __name__ == '__main__':
    print('starting program...')
    choice= int(input('Choose a option to draw: \n 1 to triangle \n 2 to square \n 3 to diamond:  '))
    draw(choice)
    print('finishing program...')