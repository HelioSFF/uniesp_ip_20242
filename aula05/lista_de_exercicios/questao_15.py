from datetime import datetime

def viagem_no_tempo(ener,localx,localy,time):
    if ener >= 80:
        print(f'Energia de {ener}%')
        print(f'Energia checada!')
        return True
    else:
        print(f'Energia de {ener}%')
        print("Energia insulficiente")
        return False
    
    if localx == float and localy == float:
        print(f'Coordenadas detectadas x:{localx} y: {localy}')
        return True
    else:
        print('Coordenadas invalidas')
        return False
    
    if time == datetime.strftime(time, "%H: %M:"):
        print("Hora confirmada")
        return True
    else:
        print("Hora invalida")
        return False
    
    if ener == True and localx == True and localy == True and time == True:
        print("Viagem confirmada!")

    else:
        print("Algo deu errado")


if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    viagem_no_tempo(80,8,70,2300)


    print('--- --- Terminando o programa --- ---')