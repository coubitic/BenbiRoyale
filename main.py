from os import sys
from pymongo import MongoClient
from game import game
from utils import isInputValid, show_leaderboard, print_list, get_user_input
MAIN_MENU = ["Lancer le jeu",
            "Afficher les scores",
            "Quitter"]
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
    mode_choice = get_user_input(MAIN_MENU)
    start_mode(mode_choice)

# --- LANCEMENT DU MODE ---
# 1 = lancer le jeu, 2 = leaderboard, 3 = sys.exit()
def start_mode(mode):
    if mode == 1:
        game()
    elif mode == 2:
        show_leaderboard()
    else:
        print("Fin du jeu :'(")
        sys.exit()

start()