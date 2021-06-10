# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:24:22 2021

@author: Sofii
"""

import random
from collections import Counter

def tirada_conv():
    #Tiro los 5 dados por primera vez
    tirada1= Counter([random.randint(1,6) for i in range(5)]) 
    #Veo cual es el maximo de veces que se repite algún dado
    rep_dado1 = max((tirada1).values())
    #Hago una lista con los dados que se repiten el maximo de veces
    dados_max1 = [dado for dado in tirada1 if tirada1[dado] == rep_dado1]
    #De la lista anterior me quedo con el primero de la lista, sería la versión
    #en la cuál cuando salen todos los dados distintos me quedo con 1
    dados_max1 = dados_max1[0] 
   # print(f'Me quedo con el {dados_max1} y tengo {rep_dado1}')
    if rep_dado1 == 5: #Si es generala servida devolve un 6 y no sigas con el programa
        return 6
    tirada2= Counter([random.randint(1,6) for i in range((5-rep_dado1))])
   # print(tirada2)
    #Hago la segunda tirada solo con los dados que no me quedé
    rep_dado2 = max((tirada2).values())
   # print("max=", rep_dado2)
    #Veo cual es el máximo de veces que se repite algún dado en la segunda tirada
    if rep_dado2 == 5: #Si es generala devolve un 5
        return rep_dado2
    if rep_dado2 <= rep_dado1: 
        #Si el numero de dados repetidos en la segunda tirada es menor que en 
        # la primera, me quedo con los dados de la primera Ej: Primer tirada me 
        #quedaron 2 dados con el numero 4, y en la segunda me salieron 2 o 1 
        #dado/s con el número 3, me quedo los del numero 4 
        for dado in tirada2:
            if dado == dados_max1:
                #print(dado)
                #print(rep_dado1)
                rep_dado1+=1
                #Para cada dado en la segunda tirada, si el dado es del mismo
                #tipo que el que estaba guardando, sumo uno a la cantidad de
                #dados que guardo
      #  print(f'Ahora tengo {rep_dado1} del numero {dados_max1}')
        tirada3= Counter([random.randint(1,6) for i in range((5-rep_dado1))])
        #Hago la tercer tirada
       # print(tirada3)
        for dado in tirada3:
            if dado == dados_max1:
                #print(dado)
                #print(rep_dado1)
                rep_dado1+=1
                #Para cada dado en la tercer tirada, si el dado es del mismo
                #tipo que el que estaba guardando, sumo uno a la cantidad de
                #dados que guardo
        #print(f'Ahora tengo {rep_dado1} del numero {dados_max1}')
        return rep_dado1 # Me devuelve el numero maximo de dados del mismo numero
                         # que junte en las tres tiradas
    else:
        #Si el numero de dados repetidos en la segunda tirada es mayor que en 
        # la primera, me quedo con los dados de la segunda Ej: Primer tirada me 
        #quedaron 2 dados con el numero 4, y en la segunda me salieron 3 dados 
        #con el número 3, me quedo los del numero 3 
        
        dados_max1 = [dado for dado in tirada2 if tirada2[dado] == rep_dado2]
        dados_max1 = dados_max1[0]
        #print(f'Cambio los dados y me quedo con {dados_max1} y tengo {rep_dado2}')
        tirada3= Counter([random.randint(1,6) for i in range((5-rep_dado2))])
        for dado in tirada3:
            if dado == dados_max1:
                #print(dado)
                #print(rep_dado1)
                rep_dado2+=1
       # print(f'Ahora tengo {rep_dado2} del numero {dados_max1}')
                
        return rep_dado2 # Me devuelve el numero maximo de dados del mismo numero
                         # que junte en las tres tiradas, en el caso de quedarme
                         # con los dados de la segunda tirada
tirada_conv()

def es_generala(tirada):
    if tirada == 5:
        return "generala"
    elif tirada == 6:
        return "generala servida"

    else:
        return "Mala suerte"
print(es_generala(tirada_conv()))

N = 100000
Gc = sum([1 for i in range(N) if es_generala(tirada_conv()) == "generala"])

Gs= sum([1 for i in range(N) if es_generala(tirada_conv()) == "generala servida"])

G = Gc+Gs

probc= Gc/N
probs = Gs/N
prob = G/N
print(f'Hice {N} tiradas convencionales, de las cuales {G} saqué generala, y {Gs} fueron servidas.')
print(f'Podemos estimar la probabilidad de sacar generala mediante uno o mas tiros como: {prob:.6f}.')
print(f'Podemos estimar la probabilidad de sacar generala servida como: {probs:.6f}.')

#Para probar si tiro todos los dados de nuevo
#    if len(dados_max1)= 5 
#       tirada2 = Counter([random.randint(1,6) for i in range(5)])
