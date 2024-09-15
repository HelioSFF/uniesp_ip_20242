'''Descrição: Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se
uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3
metros). Crie um programa que receba a altura da planta e informe a sua classificação.'''

def med_plant(metro):
    if metro > 3:
        print(f"This magic plant is huge! its height is equal {metro} meters ({metro * 3.28084} ft.).")
    elif metro >= 1:
        print(f"This magic plant size is average. its height is equal {metro} meters ({metro * 3.28084} ft.).")
    else:
        print(f"This magic plant size is small. its height is equal {metro} meters ({metro * 3.28084} ft.).")


if __name__ == '__main__':

    print('--- --- Starting the program --- ---')
    med_plant(4)
    med_plant(2.5)
    med_plant(0.5)

    print('--- --- Finishing the program --- ---')
