'''Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
a. Imprima o resultado da soma de todos os valores da matriz no terminal;
b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;'''

import random

def matrix_randomica():
    a = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]

    soma = sum(sum(row) for row in a)
    print("Soma de todos os valores da matriz A:", soma)
    print(a)

    b = [[value * 3 for value in row] for row in a]
    print(b)

if __name__ == '__main__':
    print('/----------------------------------------Starting program ------------------------/')
    matrix_randomica()
    print('/----------------------------------------Finishing program ------------------------/')
