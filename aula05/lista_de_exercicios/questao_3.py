def mago_animal(animal):
    if animal == "Mamífero" or animal == "mamífero":
        print("Então seu animal favorito é o cachorro!")
        ad = input("Eu estou certo?: S/N  ")
        if ad == "S" or ad == "s":
            print("Ahá! eu sabia!")
        else:
            print("Droga, eu acerto na proxima.")
    
    elif animal == "Réptil" or animal == "réptil":
        print("Então seu animal favorito é a tartaruga!")
        ad = input("Eu estou certo?: S/N  ")
        if ad == "S" or ad == "s":
            print("Ahá! eu sabia!")
        else:
            print("Droga, eu acerto na proxima.")
    else:
        print("Eu não sei que animal é esse..")

if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')


    mago_animal(input("Qual seu tipo de animal favorito entre mamífero e réptil?: "))
    


    print('--- --- Terminando o programa --- ---')