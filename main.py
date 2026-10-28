from os import sys
from pymongo import MongoClient
from game import game
from utils import isInputValid, show_leaderboard

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