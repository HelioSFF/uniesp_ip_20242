def viagem(agua,km):
    if agua/2 == km and agua > 0:
        print("Você consegue viajar até o oásis")
    elif (agua/2) != km and agua > 0:
        print("Não possivel chegar até o oásis")
    else:
        print("Dados invalidos")

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    viagem(5,5)
    viagem(10,5)
    viagem(-1,10)



    print('--- --- Terminando o programa --- ---')