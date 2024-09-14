def dragon_race(dragon_distance1,dragon_time1,dragon_distance2,dragon_time2):
    if dragon_distance1/dragon_time1 == dragon_distance2/dragon_time2 and dragon_distance1/dragon_time1 > 0 and dragon_distance2/dragon_time2 > 0:
        print(f'They had the same speed {dragon_distance1/dragon_time1:.2f} mps!')

    elif dragon_distance1/dragon_time1 > dragon_distance2/dragon_time2 and dragon_distance1/dragon_time1 > 0 and dragon_distance2/dragon_time2 > 0:
        print(f'The first dragon was faster! It went {dragon_distance1/dragon_time1:.2f} mps')

    elif dragon_distance1/dragon_time1 < dragon_distance2/dragon_time2 and dragon_distance1/dragon_time1 > 0 and dragon_distance2/dragon_time2 > 0:
        print(f'The second dragon was faster! It went {dragon_distance2/dragon_time2:.2f} mps')

    else:
        print("Something went wrong.")


if __name__ == '__main__':

    print('--- --- Iniciando o programa --- ---')

    dragon_race(10,3,20,40)
    dragon_race(10,10,10,10)
    dragon_race(10,3,10,2)
    dragon_race(0,10,10,2)
    


    print('--- --- Terminando o programa --- ---')