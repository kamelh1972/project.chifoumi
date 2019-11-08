# -*- coding: utf-8 -*-

###creation du jeu "chifoumi"
### l'ordinateur joue au hasard
###demande pseudo a l'utilisateur

from random import randint

def choisir (number):
    if number == 1:
        print("pierre", end =' ')
    elif number == 2:
        print("feuille", end =' ')
    else:
        print("ciseau", end =' ')

###metrre a jour les scores des joueurs
def augmenter_scores(player_choice,computer_choice):
    global player_score,computer_score
    if player_choice == 1 and computer_choice == 2:
        computer_score += 1
    elif player_choice == 2 and computer_choice == 1:
        player_score += 1
    elif player_choice == 1 and computer_choice == 3:
        player_score += 1
    elif player_choice == 3 and computer_choice == 1:
        computer_score += 1
    elif player_choice == 3 and computer_choice == 2:
        player_score += 1
    elif player_choice == 2 and computer_choice == 3:
        computer_score +=1



####deroulement de la partie
continuer = True
while continuer:
    computer_score = 0
    player_score = 0
    fin = 3
    while True:
        try:
            pseudo = input("enter your Pseudo please")
            if pseudo.isalpha() and len(pseudo) < 10:
                break
        except:
                pass
        print("votre Pseudo doit avoir moins de 10 lettres et ne comporter que des lettres")
    print(pseudo)
    print ("choisissez entre pierre-feuille-ciseau.Le premier arrivé à ",fin,"à gagné")
    manche = 0
    while player_score < fin and computer_score < fin:
        computer_choice = int (input ( "1 : pierre, 2 : feuille, 3 : ciseau "))
        while computer_choice < 1 or computer_choice > 3:
            computer_choice = int(input("1 : pierre, 2 : feuille, 3 : ciseau"))

        print("vous choisissez",end=" ")
        choisir(computer_choice)
        player_choice = randint(1, 3)
        print("- Je choisis", end=" ")
        choisir(player_choice)
        print()
        if player_choice == 1 and computer_choice == 2:
            print("vous gagnez")
        elif player_choice == 2 and computer_choice == 1:
            print ("vous perdez")
        elif player_choice == 1 and computer_choice == 3:
            print ("vous perdez")
        elif player_choice == 3 and computer_choice == 1:
            print ("vous gagnez")
        elif player_choice == 3 and computer_choice == 2:
            print( "vous perdez")
        elif player_choice == 2 and computer_choice == 3:
            print("vous gagnez")
        else:
            print("egalité")

        augmenter_scores(player_choice, computer_choice)
        print("vous",computer_score, "   computer",player_score)

    choix = input("Voulez vous continuer ? ")
    if choix not in ('o', 'oui', 'ok'):
        continuer = False
