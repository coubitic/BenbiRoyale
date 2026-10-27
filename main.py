# gère le menu principal, les interactions de l'utilisateur, la sélection de l'équipe, etc
# dans les commentaires: !! instruction !! signifie que cette instruction sera une fonction à part entière

# --- FONCTION INTRODUCTION ---
# message d'introduction
# boucle infini (mode choisi sort de la boucle)
    # MENU = ["Lancer Jeu", "Afficher les scores", "Quitter"]
    # !! afficher le menu !!
    # choix = !! récupérer input de l'utilisateur !!
    # si !! input valide(choix, MENU): !!
        # mode_choisi = choix
    # sinon:
        # message d'erreur
    # !! lancement du mode(choix) !!

# fonction afficher le menu
#   boucle qui parcoure les élements de la liste menu:
#       print index de l'element + 1 et texte element

# fonction récupérer input de l'utilisateur
#   choix = input("...")
#   return choix

# fonction input valide(choix, tableau):
#   si !! choix n'est pas int !!:
#       return false
#   return int(choix) >= 0 and int(choix) =< len(tableau)
#   (pas de conflit de type car si on en arrive à cette ligne c forcement que choix est convertissable en int)

# fonction n'est pas int (choix):
#   try choix = int(choix):
#       return True
#   except:
#       return False

# --- LANCEMENT DU MODE ---
# si mode == 1:
#   fonction game
# ou si mode ==2:
#   fonction score
# ou si mode == 3:
#   sys.exit()


# fonction afficher les scores
#   liste_scores = !! recuperer scores base !!
#   trier liste_scores
#   recuperer les 3 derniers éléments du tableau
#   print ...

# fonction recuperer scores base
#   acceder à la collection score
#   find
#   convertir curseur en liste
#   return la liste