# créer les classes pour les héros et les monstres

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["BenbiRoyale"]

def data_init(collection):
    cursor = db[collection].find({},{'_id':0})
    database_collection = [char for char in cursor]
    characters_list = []
    for char in database_collection:
        char = Character(char['nom'], char['pv'], char['att'], char['def'])
        characters_list.append(char)
    return characters_list

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense


    def __str__(self):
        return (f"{self.name} - PV : {self.hp} | ATT : {self.attack} | DEF - {self.defense}")
