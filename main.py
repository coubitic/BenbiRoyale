from os import sys

# gère le menu principal, les interactions de l'utilisateur, la sélection de l'équipe, etc
# dans les commentaires: !! instruction !! signifie que cette instruction sera une fonction à part entière

# --- FONCTION INTRODUCTION ---
# message d'introduction
# boucle infini (mode choisi sort de la boucle)
    # MENU = ["Lancer Jeu", "Afficher les scores", "Quitter"]
    # !! afficher le menu !!
    # recuperer le choix de l'utilisateur
    # si !! input valide(choix, MENU): !!
        # mode_choisi = choix
    # sinon:
        # message d'erreur
    # !! lancement du mode(choix) !!

def start():
    print("Bienvenue dans BENBI ROYALE !\n")
    while True:
        menu = ["Lancer le jeu",
                "Afficher les scores",
                "Quitter"]
        print_list(menu)
        choice = input("\n Veuillez choisir une option.")
        if isInputValid(choice, menu):
            start_mode(choice)
        else:
            print("Entrée invalide ! Veuileez réessayer.")


# fonction afficher le menu
#   boucle qui parcoure les élements de la liste menu:
#       print index de l'element + 1 et texte element
def print_list(list):
    for i in list:
        print(f"{i}. list[i]")

# fonction input valide(choix, tableau):
#   si !! choix n'est pas int !!:
#       return false
#   return int(choix) >= 0 and int(choix) =< len(tableau)
#   (pas de conflit de type car si on en arrive à cette ligne c forcement que choix est convertissable en int)
def isInputValid(input, tab):
    if not isInt(input):
        return False
    return int(input) >= 0 and int(choix) <= len(tab)-1

# fonction n'est pas int (choix):
#   try choix = int(choix):
#       return True
#   except:
#       return False
def isInt(input):
    try:
        input = int(input)
        return True
    except ValueError:
        return False

# --- LANCEMENT DU MODE ---
# si mode == 1:
#   fonction game
# ou si mode ==2:
#   fonction score
# ou si mode == 3:
#   sys.exit()
def start_mode(mode):
    if mode == 1:
        game()
    elif mode == 2:
        show_leaderboard()
    else:
        sys.exit()


# fonction afficher les scores
#   liste_scores = !! recuperer collection !!
#   trier liste_scores
#   recuperer les 3 derniers éléments du tableau
#   print ...
def show_leaderboard():
    scores = get_scores()
    

# fonction recuperer collection
#   acceder à la collection 
#   find
#   convertir curseur en liste
#   return la liste
def get_scores():
    