'''Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se
um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se
completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe
10 moedas de ouro. Crie um programa que receba o número de missões completadas e
informe o valor do bônus.'''

def knight_reward(qmissions):
    if qmissions > 10:
        print(f'This knight completed {qmissions}, so the knight earned 100 gold coins')
    elif qmissions >= 5:
        print(f'This knight completed {qmissions}, so the knight earned 50 gold coins')
    elif qmissions < 5:
        print(f'This knight completed {qmissions}, so the knight earned 10 gold coins')
    else:
        print(f'Something is wrong with this knight...')
    
if __name__ == '__main__':

    print('--- --- Starting the program --- ---')

    while True:
        quest = int(input("Welcome to the guild, sir knight. How many quests did you complete?: "))
        if quest > 0:
            knight_reward(quest)
        else:
            print("Oh? You don't have any quests completed, do you?")
            break
    


    print('--- --- Finishing the program --- ---')
