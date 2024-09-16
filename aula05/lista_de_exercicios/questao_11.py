'''Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo
governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
que há um empate.'''

def royal(m1,m2,m3):
    if m1 > m2 and m1 > m3:
        print(f'O primeiro candidato ganhou com a média {m1}')
    elif m2 > m1 and m2 > m3:
        print(f'O segundo candidato ganhou com a média {m2}')
    elif m3 > m1 and m3 > m2:
        print(f'O terceiro candidato ganhou com a média {m3}')
    else:
        print("Houve um empate")

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    royal(10,3,5)
    

    print('--- --- Terminando o programa --- ---')