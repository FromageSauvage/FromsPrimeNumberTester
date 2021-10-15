from time import sleep
from math import *

#Testeur de nombres premiers de Fromage - Valentin R (opensource)

while True:
    nombre = int(input("#Raw From's prime number tester#    Nombre : "))
    print(" ")
    boucle = 2
    modulor = 0
    premier = 0
    continuer = 1
    reach = sqrt(nombre)
    while boucle < reach:
        modulor = nombre % boucle
        if modulor > 0:
            if continuer == 1:
                premier = 1
            boucle = boucle + 1
        if modulor == 0:
            continuer = 0
            premier = 0
            boucle = boucle + 1
    
    if premier == 1:
        print(f"{nombre} n'est pas divisible")
        print(f"Alors : {nombre} est un nombre premier")
        print(" ")
    
    if premier == 0:
        boucle = 2
        while boucle < reach:
            modulor = nombre % boucle
            if modulor > 0:
                    boucle = boucle + 1
            if modulor == 0:
                print(f"{nombre} est divisible par {boucle} et par {int(nombre/boucle)}")
                print(" ")
                sleep(0.5)
                boucle = boucle + 1
    
        print(f"Alors : {nombre} n'est pas un nombre premier")
        print(" ")
