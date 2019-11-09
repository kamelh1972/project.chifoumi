###creating a code that asks the user to play "CHIFUMI" with the computer
### for the choice of the computer, we will need the library 'Randum' and the module 'Randint' which we will use here to the random choice of the computer
######define the function of the choices 'here for example sheet = 1
##### the "end" function allows us to tell python that there will be an element to insert late
from random import randint
def choose (number):
    if number == 1:
        print("pierre", end =' ')
    elif number == 2:
        print("feuille", end =' ')
    else:
        print("ciseau", end =' ')
###setting of the recording and the update of the scores
####here we will create a function that will take into account 2 elements"choice of the player, choice of the computer"
####we will use the function "Global" in which it is declared 2 elements "player_score and computer_score" this function will allow us to use it in the whole of our program.
####in this case we will also use the comparator method for choices and scores.
def increase_the_scores(player_choice,computer_choice):
    global player_score,computer_score
    if player_choice == 1 and computer_choice == 2 or player_choice == 3 and computer_choice == 1 or  player_choice == 2 and computer_choice == 3:
        computer_score += 1
    elif player_choice == computer_choice:
        pass
    else:
        player_score +=1
#### in this paragraph we put the codewe will use the 'while' loops to allow the game to last 3 rounds and ask the player again if they want to continue or not
######the 'try' and the except 'allow us to manage an error occured during the insertion of the pseudo of the user
######the loop "keep _on_going" allows us to ask the users if they want to continue or leave the game
keep_on_going = True
while keep_on_going:
    computer_score = 0
    player_score = 0
    end_game = 3
    while True:
        try:
            pseudo = input("enter your Pseudo please")
            if pseudo.isalpha() and len(pseudo) < 10:
                break
        except:
                pass
        print("your Nickname must be less than 10 letters and contain only letters")
    print(pseudo)
    print ("choose between stone-leaf-chisel.The first arrived at ", end_game," won")
    manche = 0
    while player_score < end_game  and computer_score < end_game:
        computer_choice = int (input ( "1 : pierre, 2 : feuille, 3 : ciseau "))
        while computer_choice < 1 or computer_choice > 3:
            computer_choice = int(input("1 : pierre, 2 : feuille, 3 : ciseau"))
        print("vous choisissez",end=" ")
        choose(computer_choice)
        player_choice = randint(1, 3)
        print("- Je choisis", end=" ")
        choose(player_choice)
        print()
        if player_choice == 1 and computer_choice == 2 or player_choice == 3 and computer_choice == 1 or player_choice == 2 and computer_choice == 3:
            print("vous gagnez")
        elif player_choice == computer_choice:
            print("égalité")
        else:
            print(" vous perdez")
        increase_the_scores(player_choice, computer_choice)
        print("vous",computer_score, "   computer",player_score)
    choice = input("do you want to continue? ")
    if choice not in ('o', 'oui', 'ok'):
        keep_on_going = False
