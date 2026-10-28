from utils import isInputValid, show_leaderboard, add_score, get_user_input
from models import data_init, Character
from random import randint
from copy import deepcopy
PLAYER_OPTIONS = [
    "Attaquer !",
    "Se soigner",
    "Passer son tour"
]
BASE_HEALTH_POTIONS = 5

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
        hero_picked = get_user_input(available_heroes)
        team = update_team(team, available_heroes, hero_picked)
        available_heroes = update_available_heroes(available_heroes, hero_picked)
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
    health_potions = BASE_HEALTH_POTIONS
    waves_nb = 0
    while not isTeamDead(team):
        waves_nb += 1
        wave(team, health_potions)
        if isTeamDead(team):
            game_over(waves_nb, username)

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
def wave(team, health_potions):
    enemy = monster_pick()
    show_infos(team, enemy)
    while not isTeamDead(team) and enemy.hp > 0:
        health_potions = team_turn(team, enemy, health_potions)
        if enemy.hp > 0:
            enemy_attack(team, enemy)
        else:
            print("Victoire !")

# fonction tirage d'ennemi:
#   tire un monstre aléatoirement dans la base
#   crée une copie du monstre pour ne pas faire perdre la vie du monstre original qui pourrait retomber plus tard
def monster_pick():
    picked_monster = monsters_list[randint(0, len(monsters_list)-1)]
    enemy = deepcopy(picked_monster)
    return enemy

# fonction affichage infos(equipe, ennemi)
#   afficher nom, vie, attaque, defense du monstre
#   pour chaque hero:
#       afficher nom, vie "restants"
def show_infos(team, enemy):
    print(enemy)
    for hero in team:
        print(f"{hero.name} - {hero.hp} PV restants.")


# fonction tour de l'équipe: offre l'option au joueur entre attaquer, heal, ou passer son tour
def team_turn(team, enemy, health_potions):
    for hero in team:
        if hero.hp > 0:
            action = get_user_input(PLAYER_OPTIONS)
            if action == 1:
                hero_attack(hero, enemy)
            elif action == 2:
                hero_heal(hero, health_potions)
                health_potions -= 1
            else:
                print(f"{hero.name} se repose pour ce tour.")
    return health_potions
    

# fonction attaque de l'equipe (equipe, ennemi):
#   pour chaque hero:
#      si le hero est en vie:
#         degats = attaque du hero - defense du monstre
#         vie du monstre -= degats
#         annoncer les degats
def hero_attack(hero, enemy):
    damage = hero.attack - enemy.defense
    enemy.hp -= damage
    print(f"{hero.name} attaque {enemy.name} et lui inflige {damage} dégats !")
    if enemy.hp < 0:
        enemy.hp = 0

def hero_heal(hero, health_potions):
    if health_potions > 0:
        hero.hp += 15
        print(f"{hero.name} se soigne et récupère 15 PV ! (total: {hero.hp} PV) Il reste {health_potions-1} potions.")
    else:
        print("Erreur, il n'y a plus de potions ! Votre héros passe son tour.")

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
#   montrer le leaderboard
def game_over(waves, username):
    add_score(waves, username)
    print(f"\nFin de partie, tu as joué {waves} vagues ! WOW\n")
    show_leaderboard()