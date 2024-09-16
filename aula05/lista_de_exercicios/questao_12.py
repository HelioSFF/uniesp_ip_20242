'''Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
busque uma nova arma.'''

def arma(ata1,dur1,ata2,dur2,ata3,dur3):

    espada = ata1+dur1
    arco = ata2+dur2
    lança = ata3+dur3
    if espada > arco and espada > lança:
        if ata1 > 50 and dur1 >70:
            print('a espada vai ser a mais adequada')
    elif arco > espada and arco > lança:
        if ata2 > 50 and dur2 > 70:
            print('Um arco vai ser a arma mais edequada')
    elif lança > espada and lança > arco:
        if ata3 > 50 and dur3 > 70:
            print('A lança vai ser a melhor escolha')
    elif espada == arco and espada == lança:
        if ata1 > 50 and dur1 > 70 and ata2 > 50 and dur2 > 70 and ata3 > 50 and dur3 > 70:
            print('As armas são igualmente adequadas')
        else:
            print('Busque uma nova arma')
    else:
        print('Busque uma nova arma')


if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    arma(70,80,50,90,20,80)
    arma(70,71,70,71,70,71)
    

    print('--- --- Terminando o programa --- ---')