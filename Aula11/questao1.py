'''Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes
lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e
depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente
(guardados no vetor), ou NÃO ACHEI caso contrário.'''


def add_list():
    lista = []
    for i in range(5):
        clube = input('Digite um novo clube: ')
        clube = clube.upper()
        lista.append(clube)
    busca = input('Digite seu clube do coração: ')
    busca = busca.upper()
    find = False
    for clube in range(len(lista)):
        if lista[clube] == busca:
            find = True
    if find == True:
        print('Achei!')
    else:
        print('Não achei')


if __name__ == '__main__':
    print('/----------------------------------------Starting program ------------------------/')
    add_list()
    print('/----------------------------------------Finishing program ------------------------/')

    
