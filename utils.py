from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["BenbiRoyale"]


# fichier stockant les fonctions d'utilités générales, utilisées dans plusieurs autres fichiers (affichage, vérifications, etc)

# fonction input valide(choix, tableau):
#   si !! choix n'est pas int !!:
#       return false
#   return int(choix) > 0 and int(choix) <= len(tableau)
#   (pas de conflit de type car si on en arrive à cette ligne c forcement que choix est convertissable en int)
def isInputValid(input, tab):
    if not isInt(input):
        return False
    return int(input) > 0 and int(input) <= len(tab)

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


# fonction qui affiche une ligne proprement ligne par ligne
#   boucle qui parcoure les élements de la liste:
#       print index de l'element + 1 et texte element
def print_list(list):
    i = 0
    for index in list:
        i+=1
        print(f"{i}. {index}")


# fonction afficher les scores
#   liste_scores = !! recuperer collection !!
#   afficher la liste proprement
def show_leaderboard():
    leaderboard = get_best_scores()
    print("\n ----- CLASSEMENT MEILLEURS SCORES -----")
    position = 0
    for line in leaderboard:
        position += 1
        print(f"{position}. {line['player_name']}: {line['waves']} vagues")

# fonction recuperer collection
#   acceder à la collection 
#   find les 3 meilleurs scores
#   convertir curseur en liste
#   return la liste
def get_best_scores():
    scores_list = []
    scores_collection = db["scores"]
    scores_cursor = scores_collection.find({},{"_id":0})
    best_scores = scores_cursor.sort("waves",-1).limit(3)
    for score in best_scores:
        scores_list.append(score)
    return scores_list

def add_score(waves, username):
    new_score = {
        "player_name": username,
        "waves": waves
    }
    db["scores"].insert_one(new_score)

def get_user_input(tab):
    from InquirerPy import inquirer
    action = inquirer.select(
        message="Veuillez sélectionner une option : ", 
        choices=tab,
        default=None
        ).execute() 
    return tab.index(action)+1