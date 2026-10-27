from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["BenbiRoyale"]
personnages = db["personnages"]
monstres = db["monstres"]

personnages.delete_many({})
monstres.delete_many({})


personnages.insert_many([
    {"nom": "Guerrier", "att": 25, "def": 10, "pv": 100},
    {"nom": "Mage", "att": 30, "def": 5, "pv": 80},
    {"nom": "Archer", "att": 28, "def": 7, "pv": 90},
    {"nom": "Voleur", "att": 32, "def": 8, "pv": 85},
    {"nom": "Paladin", "att": 24, "def": 12, "pv": 110},
    {"nom": "Sorcier", "att": 35, "def": 3, "pv": 70},
    {"nom": "Chevalier", "att": 27, "def": 15, "pv": 120},
    {"nom": "Moine", "att": 29, "def": 9, "pv": 95},
    {"nom": "Berserker", "att": 33, "def": 6, "pv": 105},
    {"nom": "Chasseur", "att": 26, "def": 11, "pv": 100}
])


monstres.insert_many([
    {"nom": "Gobelin", "att": 10, "def": 2, "pv": 50},
    {"nom": "Orc", "att": 20, "def": 5, "pv": 120},
    {"nom": "Dragon", "att": 35, "def": 12, "pv": 300},
    {"nom": "Zombie", "att": 12, "def": 3, "pv": 70},
    {"nom": "Troll", "att": 25, "def": 10, "pv": 200},
    {"nom": "Spectre", "att": 18, "def": 7, "pv": 100},
    {"nom": "Golem", "att": 15, "def": 15, "pv": 250},
    {"nom": "Vampire", "att": 22, "def": 8, "pv": 150},
    {"nom": "Loup-garou", "att": 28, "def": 9, "pv": 180},
    {"nom": "Squelette", "att": 15, "def": 3, "pv": 90}
])