import requests as re
from loguru import logger
from time import sleep

URL = 'http://api.adviceslip.com/advice'
try:
   result = re.get(URL)
   for i in range(5):
       print(result.json()['slip']['id'])
       print(result.json()['slip']['advice'])
       id = result.json()['slip']['id']
       ad = result.json()['slip']['advice']
       with open('advice.txt', 'a', encoding='UTF-8') as arquivo:
           arquivo.write(f'{id} - {ad} \n')
       result = re.get(URL)
       sleep(1)

except Exception as e:
    logger.exception(e)

