from time import sleep


def msg_warning():
    spam = 0
    while spam < 5:
        print(f' Altere sua senha, Lembrete n° {spam}')
        spam += 1
        sleep(2)


if __name__ == '__main__':
    print('Iniciando o programa')

    msg_warning()

    print('Finalizando o programa')