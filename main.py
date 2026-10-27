# gère le menu principal, les interactions de l'utilisateur, la sélection de l'équipe, etc
# dans les commentaires: !! instruction !! signifie que cette instruction sera une fonction à part entière

# --- INTRODUCTION ---
# message d'introduction
# boucle infini (mode choisi sort de la boucle)
    # afficher le menu
    # choix = !! récupérer input de l'utilisateur !!
    # si !! input valide(choix, min, max): !!
        # retourner le mode choisi
    # sinon:
        # message d'erreur

# fonction récupérer input de l'utilisateur
#   choix = input("...")
#   return choix

# fonction input valide(choix, min, max):
#   si !! choix n'est pas int !!:
#       return false
#   return int(choix) >= min and int(choix) =< max 
#   (pas de conflit de type car si on en arrive à cette ligne c forcement que choix est convertissable en int)

# fonction n'est pas int (choix):
#   try choix = int(choix):
#       return True
#   except:
#       return False




# --- CHOIX DE L'EQUIPE ---
# equipe = []
# heros_disponibles = !! recuperer tous les heros !!
# tant que non !! équipe complète (équipe) !!:
#   tant que !! input non valide !! (choix):
#       !! afficher la liste des héros disponibles (heros disponibles) !!
#       choix = !! récuperer l'input de l'utilisateur !!
#       si !! input valide(hero_choisi, min, max): !!
#           hero_choisi = recuperer_hero(choix)
#           equipe = !! update equipe (equipe, hero_choisi) !!
#           heros_disponibles = !! update liste des heros disponible (heros_disponibles, hero_choisi) !!
#       sinon:
#           message d'erreur input non valide
# retourner équipe
# fonction equipe complete(equipe):
#   return len(equipe) == 3:

# recuperer tous les heros
#   A FAIRE PLUS TARD quand y'aura les classes etc

# fonction afficher liste des héros disponbiles
#   for hero in heros_disponibles:
#       ...

# fonction update equipe(equipe, hero_choisi)
#   equipe.append(hero_choisi)
#   return equipe   

# fonction update liste heros disponibles
#   