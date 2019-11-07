# -*- coding: utf-8 -*-

###creation du jeu "chifoumi"
### l'ordinateur joue au hasard
###demande pseudo a l'utilisateur

from random import randint

def choisir (nombre):
    if nombre == 1:
        print("pierre", end =' ')
    elif nombre == 2:
        print("feuille", end =' ')
    else:
        print("ciseau", end =' ')

###metrre a jour les scores des joueurs
def augmenter_scores(mon_coup,ton_coup):
    global mon_score,ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_score +=1

####deroulement de la partie
ton_score = 0
mon_score = 0
fin = 3
print(input("enter your usename"))
print ("pierre-feuille-ciseau.Le premier arrivé à ",fin,"à gagné")
manche = 0
while mon_score < fin and ton_score < fin:
    ton_coup = int (input ( "1 : pierre, 2 : feuille, 3 : ciseau "))
    while ton_coup < 1 or ton_coup > 3:
        ton_coup = int(input("1 : pierre, 2 : feuille, 3 : ciseau"))
    print("vous choisissez",end=" ")
    choisir(ton_coup)
    mon_coup = randint(1, 3)
    print("- Je montre", end=" ")
    choisir(mon_coup)
    print()
    augmenter_scores(mon_coup, ton_coup)
    print("vous",ton_score, "   moi",mon_score)
