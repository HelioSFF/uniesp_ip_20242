def viagem_no_tempo(ener,localx,localy,date):
    if ener >= 80:
        print(f'Energia de {ener}%')
        print(f'Energia checada!')

        if type(localx) == float or int and type(localy) == float or int:
            print(f'Coordenadas detectadas x:{localx} y: {localy}')

            if type(date) == int:
                print(f'Ano confirmado: {date}')
                print("Viagem confirmada!")

            else:
                print("Hora invalida")

        else:
            print('Coordenadas invalidas')
    else:
        print(f'Energia de {ener}%')
        print("Energia insulficiente")
       

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    viagem_no_tempo(100,-512,2570,224)


    print('--- --- Terminando o programa --- ---')