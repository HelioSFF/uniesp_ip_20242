'''Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
considerar a defesa como critério de desempate.'''

def duelo(atq1,def1,atq2,def2):
    duelista1= atq1+def1
    duelista2= atq2+def2
    if duelista1 > duelista2:
        print('Duelista 1 vencedor')
    elif duelista2 > duelista1:
        print('Duelista 2 vencedor')
    elif duelista1 == duelista2:
        if def1 > def2:
            print('Duelista 1 vencedor')
        elif def2 > def1:
            print('Duelista 2 vencedor')
        else:
            print('Empate!')
    else:
        print('Algo deu errado')

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')
   
    duelo(7,5,2,4)
    duelo(5,6,2,9)




    print('--- --- Terminando o programa --- ---')
