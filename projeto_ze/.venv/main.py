from deep_translator import GoogleTranslator
import requests as re
import time


URL = 'https://api.adviceslip.com/advice'

def count_ad():
    try:
        qad = int(input('Digite quantos conselhos gostaria de receber: '))
        result = re.get(URL)
        for i in range(qad):
            id = result.json()['slip']['id']
            ad = result.json()['slip']['advice']
            print(f'Id: {result.json()['slip']['id']} - {result.json()['slip']['advice']}')
            with open('advice.txt', 'a', encoding='UTF-8') as arquivo:
                arquivo.write(f'{id} - {ad} \n')
            result = re.get(URL)
            sleep(1)

    except TypeError as e:
        print(f'Dado invalido: {e}')

    except Exception as e:
        print(f'Error {e}')


def show_ad():
    with open('advice.txt', 'r+', encoding='UTF-8') as arquivo:
        shad = arquivo.readlines()
        for i in shad:
            print(f'{i.strip()}')
            time.sleep(1)


def translate_ad():
    with open('advice.txt', 'r+', encoding='UTF-8') as arquivo:
        shad = arquivo.readlines()
        for i in shad:
            frase = i.strip()
            traducao = GoogleTranslator(source='auto', target='portuguese').translate(frase)
            print(traducao)
            time.sleep(1)


if __name__ == '__main__':

    op = 1

    while op != 0:
        print('1 - Pedir conselhos')
        print('2 - Mostrar conselhos')
        print('3 - Traduzir os conselhos para português')
        try:
            menu = int(input('Bem vindo ao programa de conselhos! \n Digite numero correspondente a opção desejada:   '))
            if menu == 1:
                count_ad()
                op = int(input('Digite 0 para finalizar o programa \n ou outro numero para continuar :'))
            elif menu == 2:
                show_ad()
                op = int(input('Digite 0 para finalizar o programa \n ou outro numero para continuar :'))
            elif menu == 3:
                translate_ad()
                op = int(input('Digite 0 para finalizar o programa \n ou outro numero para continuar :'))

        except TypeError as error:
            print(f'Error! Tipo de dado errado')

        except Exception as error:
            print(f'Erro - {error}')