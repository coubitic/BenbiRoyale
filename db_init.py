from pymongo import *

client = MongoClient("mongodb://localhost:27017")
db = client["PythonAdventure"]

all_monsters = db["monsters"]
all_heroes = db["heroes"]