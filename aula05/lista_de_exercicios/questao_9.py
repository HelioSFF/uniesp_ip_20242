'''Descrição: Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a
escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para
exibir o feitiço escolhido.'''
def magic(mana):
    match mana:
        case 1:
            print("You casted a fire spell!")
        case 2:
            print("You casted a water spell!")
        case 3:
            print("You casted a earth spell!")
        case _:
            print("You don't know that spell...")

if __name__ == '__main__':

    print('--- --- Starting the program --- ---')
    magic(1)
    magic(2)
    magic(3)

    print('--- --- Finishing the program --- ---')
