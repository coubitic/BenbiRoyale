# --- FONCTION CHOIX DE L'EQUIPE ---
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
# return equipe

# fonction equipe complete(equipe):
#   return len(equipe) == 3:

# recuperer tous les heros
#   A FAIRE PLUS TARD quand y'aura les classes etc

# fonction afficher liste des héros disponbiles
#   for hero in heros_disponibles:
#       ...

# fonction recuperer_hero(choix):
#   return heros_disponibles[choix-1]

# fonction update equipe(equipe, hero_choisi)
#   equipe.append(hero_choisi)
#   return equipe   

# fonction update liste heros disponibles(heros_disponibles, heros_choisi)
#   heros_disponibles.pop(hero_choisi)
#   return heros_disponibles



# --- FONCTION GAME ---
# nombre_vagues = 0
# tant que not !! equipe morte !!:
#   nombre_vagues += 1
#   !! vague !!
#   if !! equipe morte !!:
#      message de game over avec annonce du score

# fonction equipe morte:
#   boucle qui parcourt l'equipe
#       si un hero a encore de la vie, la fonction renvoie false, sinon elle renvoie true

# fonction vague:
#   ennemi = !! selection du monstre !!
#   !! affichage_infos(equipe, ennemi) !!
#   pendant que le combat n'est pas fini:
#       !! attaque de l'equipe !!
#       si le monstre n'est pas mort:
#           !! attaque du monstre !!
#   
