# créer les classes pour les héros et les monstres

# classe hero
#   nom
#   defense
#   attaque
#   vie

class Character:
    def __init__(self, name, defense, attack, hp):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.hp = hp


