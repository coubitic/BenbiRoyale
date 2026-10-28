from main import isInputValid

# --- FONCTION CREATION DE L'EQUIPE ---
# initier une liste equipe vide
# heros_disponibles = !! recuperer tous les heros !!
# tant que non !! équipe complète (équipe) !!:
#   boucle infini
#       !! afficher la liste des héros disponibles (heros disponibles) !!
#       récuperer l'input de l'utilisateur
#       si !! input valide: !!
#           equipe = !! update equipe (equipe, hero_choisi) !!
#           heros_disponibles = !! update liste des heros disponible (heros_disponibles, hero_choisi) !!
#           sort de la boucle infini pour repartir dans la boucle globale qui check si la team est complete
#       sinon:
#           message d'erreur input non valide
# return equipe

def team_create():
    team = []
    available_heroes = get_all_heroes()
    while not isTeamFull(team):
        while True:
            print_heroes(available_heroes)
            hero_pick = input("Veuillez choisir un héros !")
            if isInputValid(hero_pick, available_heroes):
                team = update_team(team, hero_pick)
                available_heroes = update_available_heroes(available_heroes, hero_pick)
                break
            else:
                print("Erreur: veuillez entrer un nombre valide.")


# fonction equipe complete(equipe):
#   return len(equipe) == 3:
def isTeamFull(team):
    return len(team) == 3

# recuperer tous les heros
#   A FAIRE PLUS TARD quand y'aura les classes etc


# fonction afficher liste des héros disponbiles
#   for hero in heros_disponibles:
#       ...
def print_heroes(heroes):
    for hero in heroes:
        ...


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