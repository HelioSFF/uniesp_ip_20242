'''Descrição: O sistema de defesa de um castelo mágico precisa estar sempre ativo quando o
exército do rei está fora. Crie um programa que receba a posição do exército (dentro ou fora
do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente.'''

def sistema_de_defesa(posicao):
    match posicao.lower():
        case 'dentro':
            print('Sistema de defesa desativado')
            if posicao == 'dentro':
                x= input('Deseja sair? Sim ou Nao:   ').lower()
                if x == 'sim':
                    print('Sistema de defesa ativado')

        case 'fora':
            print('Sistema de defesa ativado')
            if posicao == 'fora':
                x= input('Deseja entrar? Sim ou Nao').lower()
                if x == 'sim':
                    print('Sistema de defesa desativado')
        case _:
            print('Invalido')

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')
    posi = input("Digite a posição do exercito do rei: dentro ou fora   ")
    sistema_de_defesa(posi)




    print('--- --- Terminando o programa --- ---')