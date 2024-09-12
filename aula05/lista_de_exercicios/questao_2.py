def forgar_armadura(fe,au):
    if (au/fe)*100 >= 30:
        print('Sua armadura tem uma liga metalica boa')
    elif (au/fe)*100 < 30:
        print("Não tem ferro o suficiente")
    else:
        print("Quantidade de metal invalido")


if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    forgar_armadura(80,23)


    print('--- --- Terminando o programa --- ---')