'''Descrição: Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.'''
import random
import sys

def cave(door):
    print("Status")
    hp = random.randrange(0, 20)
    print(f'Health Points = {hp}')
    strength = random.randrange(0, 20)
    print(f'Str = {strength}')
    dex = random.randrange(0, 20)
    print(f'Dex = {dex}')
    speed = random.randrange(0, 20)
    print(f'Speed = {speed}')
    luk = random.randrange(0, 20)
    print(f'Luck = {luk}')

    match door:
        case 1:
            print('You open the door number 1 and find a group of goblins... they are sleeping but you can see a chest in the end of the room ')
            print('What do you want to do? Type "1" to try to sneak between the sleepling goblins to get the chest for yourself')
            print('or Type "2" to try to get them one by one then take the prize inside the chest')
            choice = int(input("What is your choice?: "))
            #first choice of case 1 (start)
            if choice == 1:
                print('So... you want to sneak between them and get the chest.')
                challdex= random.randrange(0, 20)
                #testing player's dex
                if dex > challdex:
                    print('You have enough dexterity to sneak around them')
                    choice2 = int(input('Do you want to continue and try to open the chest? (Type 1 to "Yes" or Type 2 to "No"): '))
                    #Second choice of case 1 (start)
                    if choice2 == 1:
                        print('You decided to continue..')
                        print('You try to open the chest but the squeaky wood make some noise')
                        challluk= random.randrange(0, 20)
                        #testing player's luck
                        if luk > challluk:
                            print('You opened the chest! there are lots of gold there!')
                            print('You do your best go take everything without wake them up and flee with the treasure')
                            print('You survived the cave with your gold... this time...')
                        else:
                            print('The sound of the wood woke the goblins up!')
                            challspeed= random.randrange(0, 20)
                            #lost the luck test
                            if speed > challspeed:
                                print('You are able to atack them first!')
                                challstr= random.randrange(0, 20)
                                #testing player's strenght
                                if strength > challstr:
                                    print('You fought them are end up victorious!')
                                    print('You take the treasure and exit the cave alive!')
                                    print('You survived the cave with your gold... this time...')
                                #lost the game
                                else:
                                    print('You have been overwhelmed by the goblins... good luck next time!')
                            else:
                                print("They are faster than you thought!")
                                challstr= random.randrange(0, 20)
                                #testing if the player is going to survive
                                if hp > challstr:
                                    print('You hurried up to flee from the goblins')
                                    print('You survived the cave injured... and without your treasure...')
                                #lost the game    
                                else:
                                    print('You have been defeated by the goblins... good luck next time!')
                    else: #Second choice of case 1 (end)
                        print('After looking around how old and dusty the chest is you ponder if it is worth the risk ')
                        challluk= random.randrange(0, 20)
                        #testing player's luck
                        if luk > challluk:
                            choice3 = int(input(('You find lever! do you want to push it? Type 1 to "Yes" or Type 2 to "No" : ')))
                            if choice3 == 1:
                                print("You pushed the lever")
                                print("The whole place shakes and suddenly a big boulder drops onto the goblins")
                                print('Since you feel safe you get the chest and exit the cave')
                                print('You survived the cave with your gold... this time...')
                            elif choice == 2:
                                print('You decided that it is not worth it')
                                print('You exit the cave and you survived the cave.... this time')
                            else:
                                print('Invalid choice')
                #lost the dex test                
                else:
                    print('You woke up one of those goblins and it grabbed your leg!')
                    challstr= random.randrange(0, 20)
                    challdex= random.randrange(0, 20)
                    if strength > challstr and dex > challdex:
                        print('You squashed the goblins head without letting him do any noise')
                        choice2 = int(input('Do you want to continue and try to open the chest?: (Type 1 to "Yes" or Type 2 to "No")'))
                        if choice2 == 1:
                            print('You decided to continue..')
                            print('You try to open the chest but the squeaky wood make some noise')
                            challluk= random.randrange(0, 20)
                            if luk > challluk:
                                print('You opened the chest! there are lots of gold there!')
                                print('You do your best go take everything without wake them up and flee with the treasure')
                                print('You survived the cave with your gold... this time...')
                            else:
                                print('The sound of the wood woke the goblins up!')
                                challspeed= random.randrange(0, 20)
                                if speed > challspeed:
                                    print('You are able to atack them first!')
                                    challstr= random.randrange(0, 20)
                                    if strength > challstr:
                                        print('You fought them are end up victorious!')
                                        print('You take the treasure and exit the cave alive!')
                                        print('You survived the cave with your gold... this time...')
                                    else:
                                        print('You have been overwhelmed by the goblins... good luck next time!')
                                else:
                                    print("They are faster than you thought!")
                                    challstr= random.randrange(0, 20)
                                    if hp > challstr:
                                        print('You hurried up to flee from the goblins')
                                        print('You survived the cave injured... and without your treasure...')
                                    else:
                                        print('You have been defeated by the goblins... good luck next time!')
                    elif strength > challstr:
                        print('You had enough strength to flee of that goblins grasp')
                        print('You run for your life but you survived the cave.... this time')
                    else:
                        print('The goblin cries to awaken the others!')
                        print('You have been overwhelmed by the goblins... good luck next time!')
            elif choice == 2:
                print('There are 5 goblins sleeping on the floor and you decide to take them while sleeping')
                goblins = 5
                for i in range(goblins):
                    challdex = random.randrange(0, 20)
                    if dex > challdex:
                        print(f'You got the goblin {i+1}')
                    else:
                        print("You were overwhelmed by the goblins")
                        print('Game over.')
                        sys.exit()
                # Check if all goblins were defeated
                if i + 1 == goblins:
                    print('You were able to defeat all of them!')
                    print('You survived the cave with the gold..... this time')


            else:
                print("Invalid choice")
        #Checking case 2 ----------------------------------------------------------------------------------------------------------------------------------------------
        case 2:
            print('You open the second door and find a weird looking man asking you for help')
            choice2_1= int(input('Do you want to help him or leave the cave? Type "1" to help or Type "2" to leave:  '))
            #first choice of the case 2
            if choice2_1 == 1:
                print('You rushed to help the man')
                print(' ')
                print('Weird man : Oh, thank the goddness! my prayers were been answered! Will you help me leave here, will ya? ')
                challluk = random.randrange(0, 20)
                if luk > challluk:
                    print('You heard muffed cry behind the weird man')
                    print('Weird man :  Hey pal, lets keep going, I had enough of this place')
                    choice2_2 = int(input('Do you want to check the source of the cry or just help the man and ignore it (Type 1 to help or Type 2 to ignore ) : '))
                    #Second choice of the case 2
                    if choice2_2 == 1:
                        print('You decided the pull the man aside and check it')
                        print('The air feels tense when you find a tied up girl')
                        challspeed = random.randrange(0, 20)
                        if speed > challspeed:
                            print('Feeling that something is off, you turn to face the man and noticed that he was about to backstab you')
                            challstr = random.randrange(0, 20)
                            if strength > challstr:
                                print('You are able to hold the man arms and submit him to drop the knife')
                                print('the man screams in pain')
                                print('You noticed that the girl was watching')
                                choice2_3 = int(input('Do you want to proceed and finish off the man or rush to help the girl? Type 1 to finish off or Type 2 to help the girl  : '))
                                if choice2_3 == 1:
                                    print('You rise your weapon and with one blow you finish off the man')
                                    print('The girl cries, you rush to help her and get out of the cave')
                                    print('You survived the cave and helped the girl...')
                                elif choice2_3 == 2:
                                    print('You rushed to help the girl ignoring the man who just tried to get you')
                                    print('You untie and grab her to get out the cave')
                                    challspeed = random.randrange(0, 20)
                                    if speed > challspeed:
                                        print('You noticed the man running in your direction but you are able to avoid him and close the door locking him in')
                                        print('You survived the cave! both of you!')
                                    else:
                                        print('You were running with the girl to get out the cave')
                                        print('Suddenly the man tackle both of you')
                                        print('Grabs and finish you off... Locking the girl and you body inside the cave')
                                else:
                                    print('Invalid Choice')
                            else:
                                print('The man overwhelms you with his strengh and put you on the ground')
                                print('You looked at the girl then you feel a heavy hit on your head')
                                print('You blacked out.')        
                        else:
                            print('Suddenly you feel a sharp pain coming from your back, it was the man with a knife')
                            print('You fell unconscious')

                    elif choice2_2 == 2:
                        print('You decided to ignore it and call it a day')
                        print('You and the man get out of the cave locking whatever was inside in')

                    else:
                        print("Invalid Choice")
                else:
                    print('You proceeded to help the man')
                    print('Bringing him to the exit')
                    print('Weird man: Oh my, better to lock this door to make everyone safe, It is too dark there. You lost yourself in easily')
                    print('You and the man leave the cave peacefully')

            elif choice2_1 == 2:
                print('You feel something off and decide to leave')
                print('You dont even enter the cave...')

            else:
                print('Invalid choice')
        # Starting the third case --------------------------------------------------------------------------------------------------------------------------------------------
        case 3:
            print('Inside the room 3 of the case you find a huge statue with glowing eyes ')
            print('You get closer to it ')
            print('It asks you to solve a riddle if you do it, The statue will allow you to take the treasure of this room')
            riddle = input('Statue: What can’t talk but will reply when spoken to?:    ')
            if riddle == "Echo" or riddle == "echo" or riddle == "an echo" or riddle == "an Echo":
                print('Statue: Humpf.... very well...')
                print('The eyes stops to glow, allowing you to be able to see the old chest under the statue')
                print('You take the treasure and get out the cave')
                print('You survived the cave with the treasure....for now')
            else:
                print('The eyes glows even stronger')
                print('The statue says "WRONG!')
                print('The light inside the cave get strong and stronger')
                print('Until you feel anything...')

        # Starting the fourth case -------------------------------------------------------------------------------------------------------------------------------------------
        case 4:
            print('You open the fourth room then you see a room with 5 more doors')
            x= int(input('Which door do you want open?:  '))
            if x == 5:
                print('You won!')
            elif x < 5:
                print('Too bad! you lost.')
            else:
                print('Are you even trying?')


        # Starting the fifth case ----------------------------------------------------------------------------------------------------------------------------------------------

        case 5:
            if dex+strength+hp+speed+luk >= 50:
                print('Great stats!')
            else:
                print('Unlucky')
    
        case _:
            print("There's not such place in the cave")
                                



if __name__ == '__main__':

    print('--- --- Starting the program --- ---')
    cave(4)

    print('--- --- Finishing the program --- ---')

