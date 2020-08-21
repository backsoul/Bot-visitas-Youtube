from selenium import webdriver
import time
from random import randrange

tiempo_vista = 5
lista_navegador = []

navegador_1 = webdriver.Chrome(executable_path='./chromedriver')
navegador_2 = webdriver.Chrome(executable_path='./chromedriver')
navegador_3 = webdriver.Chrome(executable_path='./chromedriver')

lista_navegador.append(navegador_1)
lista_navegador.append(navegador_2)
lista_navegador.append(navegador_3)

for navegador in lista_navegador:
    navegador.get('http://raboninco.com/14240325/https://tontuber.blogspot.com/2019/04/en-busca-de-la-felicidad.html')
while(True):
    numero_random = randrange(0,len(lista_navegador))
    lista_navegador[numero_random].refresh()
    print("Navegador Numero: ",numero_random,"Se a Actualizado")
    time.sleep(tiempo_vista)
