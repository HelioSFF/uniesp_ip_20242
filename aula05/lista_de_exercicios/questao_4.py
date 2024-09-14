def count_coin(qcoin1,qcoin2,qcoin3):
    if qcoin1 >= 0:
        valor = qcoin1 * 1
        print(f'Quantidades de moedas de um real é de {qcoin1}')
        if qcoin2 >= 0:
            valor += qcoin2 * 0.50
            print(f'Quantidade de moedas de cinquenta centavos é de {qcoin2}')
            if qcoin3 >= 0:
                valor += qcoin3 * 0.25
                print(f'Quantidade de moedas de vinte e quinco centavos é de {qcoin3}')
                print(f'Valor total da coleção é de {valor} R$')
            else:
                print("Quantidade invalida")
        else:
            print("Quantidade invalida")
    else:
        print("Quantidade invalida")

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')


    count_coin(10,5,3)
    count_coin(0,0,500)
    count_coin(-10,100,100)


    print('--- --- Terminando o programa --- ---')