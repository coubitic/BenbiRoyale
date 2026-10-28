from utils import isInputValid
from models import data_init, Character
from random import randint

heroes_list = data_init("personnages")
monsters_list = data_init("monstres")

# --- FONCTION CREATION DE L'EQUIPE ---
# initier une liste equipe vide
# heros_disponibles = !! recuperer tous les heros !! (fonction faite dans models.py)
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

def create_team():
    team = []
    available_heroes = heroes_list
    while not isTeamFull(team):
        while True:
            print_heroes(available_heroes)
            hero_pick = input("\nVeuillez choisir un héros !   -->  ")
            if isInputValid(hero_pick, available_heroes):
                hero_pick = int(hero_pick)
                team = update_team(team, available_heroes, hero_pick)
                available_heroes = update_available_heroes(available_heroes, hero_pick)
                break
            else:
                print("\nErreur: veuillez entrer un nombre valide.\n")
    return team

# fonction equipe complete(equipe):
#   return len(equipe) == 3:
def isTeamFull(team):
    return len(team) == 3

# fonction afficher liste des héros disponbiles
#   for hero in heros_disponibles:
#       ...
def print_heroes(heroes):
    i = 0
    for hero in heroes:
        i+=1
        print(f"{i}. {hero}")

# fonction update equipe(equipe, hero_choisi)
#   ajouter le bon heros à l'equipe avec le numero choisi -1 (pour l'index)
#   return equipe   
def update_team(team, available_heroes, hero_pick):
    team.append(available_heroes[hero_pick-1])
    return team

# fonction update liste heros disponibles(heros_disponibles, heros_choisi)
#   heros_disponibles.remove(hero_choisi)
#   return heros_disponibles
def update_available_heroes(available_heroes, hero_pick):
    available_heroes.remove(available_heroes[hero_pick-1])
    return available_heroes

# --- FONCTION GAME ---
# creation du joueur
# creation de l'equipe
# nombre_vagues = 0
# tant que not !! equipe morte !!:
#   nombre_vagues += 1
#   !! vague !!
#   si !! equipe morte !!:
#       !! fin de partie (nombre_vagues) !!
def game():
    username = create_player()
    team = create_team()
    waves_nb = 0
    while not isTeamDead(team):
        waves_nb += 1
        wave(team)
        if isTeamDead(team):
            game_over(waves_nb)

# fonction creation du joueur
#   boucle infini
#       demander de rentrer un nom
#       si !! nom valide !!
#           return nom
def create_player():
    while True:
        username = input("Bienvenue ! Veuillez entrer votre nom d'utilisateur. --->  ")
        if isNameValid(username):
            return username
        else:
            print("Nom d'utilisateur invalide ! Veuillez saisir un nom compris entre 3 et 30 lettres.")

# fonction nom valide
#   return len(nom) >= 3 and len(nom) <= 30
def isNameValid(name):
    return len(name) >= 3 and len(name) <= 30


# fonction equipe morte:
#   boucle qui parcourt l'equipe
#       si un hero a encore de la vie, la fonction renvoie false, sinon elle renvoie true
def isTeamDead(team):
    for hero in team:
        if hero.hp > 0:
            return False
    return True

# fonction vague:
#   ennemi = !! selection du monstre !!
#   !! affichage_infos(equipe, ennemi) !!
#   pendant que l'equipe n'est pas morte et l'ennemi n'est pas mort:
#       !! attaque de l'equipe !!
#       si ennemi n'est pas mort:
#           !! attaque d'ennemi !!
#       sinon:
#           dire que le combat est remporté
def wave(team):
    enemy = monster_pick()
    show_infos(team, enemy)
    while not isTeamDead(team) and enemy.hp > 0:
        team_attack(team, enemy)
        if enemy.hp > 0:
            enemy_attack(team, enemy)
        else:
            print("Victoire !")

# fonction tirage d'ennemi:
#   tire un monstre aléatoirement dans la base
#   crée une copie du monstre pour ne pas faire perdre la vie du monstre original qui pourrait retomber plus tard
def monster_pick():
    picked_monster = monsters_list[randint(0, len(monsters_list)-1)]
    enemy = picked_monster
    return enemy

# fonction affichage infos(equipe, ennemi)
#   afficher nom, vie, attaque, defense du monstre
#   pour chaque hero:
#       afficher nom, vie "restants"
def show_infos(team, enemy):
    print(enemy)
    for hero in team:
        print(f"{hero.name} - {hero.hp} PV restants.")



# fonction attaque de l'equipe (equipe, ennemi):
#   pour chaque hero:
#      si le hero est en vie:
#         degats = attaque du hero - defense du monstre
#         vie du monstre -= degats
#         annoncer les degats
def team_attack(team, enemy):
    for hero in team:
        if hero.hp > 0:
            damage = hero.attack - enemy.defense
            enemy.hp -= damage
            print(f"{hero.name} attaque {enemy.name} et lui inflige {damage} dégats !")
            if enemy.hp < 0:
                enemy.hp = 0


# fonction attaque d'ennemi (equipe, ennemi):
#   liste contenant seulement les heroes encore en vie
#   cible = hero tiré aleatoirement parmis la liste
#   degats = attaque du monstre - defense de la cible
#   vie de la cible -= degats
#   annoncer les degats effectueur
def enemy_attack(team, enemy):
    alive_heroes = [hero for hero in team if hero.hp > 0]
    target = alive_heroes[randint(0, len(alive_heroes)-1)]
    damage = enemy.attack - target.defense
    target.hp -= damage
    print(f"{enemy.name} attaque {target.name} et lui inflige {damage} dégats !")
    if target.hp < 0:
        target.hp = 0

# fonction fin de partie (nombre_vagues):
#   annoncer le resultat avec le nombre de vagues survécues
#   ajouter le score à la db


def game_over(waves):
    print(f"Fin de partie, tu as joué {waves} vagues ! WOW ")


game()