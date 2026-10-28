from os import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["BenbiRoyale"]

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
        print(f"{i+1}. {list[i]}")

# fonction input valide(choix, tableau):
#   si !! choix n'est pas int !!:
#       return false
#   return int(choix) >= 0 and int(choix) < len(tableau)
#   (pas de conflit de type car si on en arrive à cette ligne c forcement que choix est convertissable en int)
def isInputValid(input, tab):
    if not isInt(input):
        return False
    return int(input) >= 0 and int(input) < len(tab)

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
#   afficher la liste proprement
def show_leaderboard():
    leaderboard = get_best_scores()
    print("\n ----- CLASSEMENT MEILLEURS SCORES -----")
    position = 0
    for line in leaderboard:
        position+=1
        print(f"{position}. {line['player_name']}: {line['waves']} vagues")
        # bug mineur: à la fin du print du leaderboard ya une ligne "None"


# fonction recuperer collection
#   acceder à la collection 
#   find les 3 meilleurs scores
#   convertir curseur en liste
#   return la liste
def get_best_scores():
    scores_list = []
    scores_collection =  db["scores"]
    scores_cursor = scores_collection.find({},{"_id":0})
    best_scores = scores_cursor.sort("waves",-1).limit(3)
    for score in best_scores:
        scores_list.append(score)
    return scores_list


print(show_leaderboard())
