# --- FONCTION CREATION DE L'EQUIPE ---
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
#   heros_disponibles.remove(hero_choisi)
#   return heros_disponibles

# fonction creation du joueur
#   boucle infini
#       demander de rentrer un nom
#       si !! nom valide !!
#           return nom

# fonction nom valide
#   return len(nom) >= 3 and len(nom) <= 30

# --- FONCTION GAME ---
# creation du joueur
# creation de l'equipe
# nombre_vagues = 0
# tant que not !! equipe morte !!:
#   nombre_vagues += 1
#   !! vague !!
#   si !! equipe morte !!:
#       !! fin de partie (nombre_vagues) !!

# fonction equipe morte:
#   boucle qui parcourt l'equipe
#       si un hero a encore de la vie, la fonction renvoie false, sinon elle renvoie true

# fonction vague:
#   ennemi = !! selection du monstre !!
#   !! affichage_infos(equipe, ennemi) !!
#   pendant que l'equipe n'est pas morte et l'ennemi n'est pas mort:
#       !! attaque de l'equipe !!
#       si ennemi n'est pas mort:
#           !! attaque d'ennemi !!
#       sinon:
#           dire que le combat est remporté

# fonction affichage infos(equipe, ennemi)
#   afficher nom, vie, attaque, defense du monstre
#   pour chaque hero:
#       afficher nom, vie "restants"

# fonction attaque de l'equipe (equipe, ennemi):
#   pour chaque hero:
#      si le hero est en vie:
#         degats = attaque du hero - defense du monstre
#         vie du monstre -= degats

# fonction attaque d'ennemi (equipe, ennemi):
#   liste contenant seulement les heroes encore en vie
#   cible = hero tiré aleatoirement parmis la liste
#   degats = attaque du monstre - defense de la cible
#   vie du monstre -= degats

# fonction fin de partie (nombre_vagues):
#   annoncer le resultat avec le nombre de vagues survécues
#   ajouter le score à la db