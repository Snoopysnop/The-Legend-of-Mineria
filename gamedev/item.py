from enum import Enum


class Item(Enum):
    """
    equipment part
    """

    """
        weapons
    """
    epeeStylee = {"name": "epeeStylee", "lvl": 5, "description": "une epe puissante", "damage": 25,
                  "class": "guerrier", "type": "equipment", "typeOfEquipment": "weapon"}
    piocheOula = {"name": "piocheOula", "lvl": 2, "description": "une pioche febrile", "damage": 5,
                  "class": "any", "type": "equipment", "typeOfEquipment": "weapon"}
    arcBadass = {"name": "arcBadass", "lvl": 5, "description": "un arc puissant", "damage": 15, "defense": 0,
                 "class": "archer", "type": "equipment", "typeOfEquipment": "weapon"}
    batonDuDiable = {"name": "batonDuDiable", "lvl": 5, "description": "un baton puissant", "damage": 20,
                     "class": "mage", "type": "equipment", "typeOfEquipment": "weapon"}

    """
        armor
    """
    casqueCuir = {"name": "casqueCuir", "lvl": 1, "description": "casque pas tres resistant",
                  "defense": 10, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                  "typeOfArmor": "helmet"}
    plastronCuir = {"name": "plastronCuir", "lvl": 1, "description": "plastron pas tres resistant",
                    "defense": 10, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                    "typeOfArmor": "chestplate"}
    jambieresCuir = {"name": "jambieresCuir", "lvl": 1, "description": "jambieres pas tres resistantes",
                     "defense": 10, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                     "typeOfArmor": "leggings"}
    bottesCuir = {"name": "bottesCuir", "lvl": 1, "description": "bottes pas tres resistantes",
                  "defense": 10, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                  "typeOfArmor": "boots"}

    casqueMaille = {"name": "casqueMaille", "lvl": 5, "description": "casque un peu resistant",
                    "defense": 20, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                    "typeOfArmor": "helmet"}
    plastronMaille = {"name": "plastronMaille", "lvl": 5, "description": "plastron un peu resistant",
                      "defense": 20, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                      "typeOfArmor": "chestplate"}
    jambieresMaille = {"name": "jambieresMaille", "lvl": 5, "description": "jambieres un peu resistantes",
                       "defense": 20, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                       "typeOfArmor": "leggings"}
    bottesMaille = {"name": "bottesMaille", "lvl": 5, "description": "bottes un peu resistantes",
                    "defense": 20, "class": "any", "type": "equipment", "typeOfEquipment": "armor",
                    "typeOfArmor": "boots"}

    """
    resource part
    """

    bois = {"name": "bois", "lvl": 1, "price": 20, "description": "un bois sec et peu couteux", "type": "resource"}
    cuir = {"name": "cuir", "lvl": 1, "price": 15, "description": "un cuir provenant d'un goblin", "type": "resource"}
    slip = {"name": "slip", "lvl": 1, "price": 10, "description": "un slip provenant d'un guerrier redoutable",
            "type": "resource"}
    crochet = {"name": "crochet", "lvl": 2, "price": 30, "description": "un crochet venant d'un pirate celebre",
               "type": "resource"}

    """
    consumable part
    """

    poissonCru = {"name": "poissonCru", "lvl": 1, "description": "un morceau de poisson nauséabond", "value": 10,
                  "reaction": "🐟",
                  "stats": "hp", "type": "consumable"}
    painChaud = {"name": "painChaud", "lvl": 3, "description": "un pain redonnant de la vie", "value": 25,
                 "reaction": "🍞",
                 "stats": "hp", "type": "consumable"}
    potionHeal = {"name": "potionHeal", "lvl": 5, "description": "une potion redonnant de la vie", "value": 100,
                  "reaction": "🥃",
                  "stats": "hp", "type": "consumable"}

    """
        XP part
    """

    parcheminXp = {"name": "parcheminXp", "lvl": 3, "description": "un parchemin donnant de lxp", "value": 30,
                   "stats": "xp", "type": "consumable"}

    """
        Gold part
    """

    boursePieceOr = {"name": "boursePieceOr", "lvl": 2, "description": "une bourse de pieces d'or", "value": 50,
                     "stats": "gold", "type": "consumable"}

    def getName(self):
        return self.value["name"]

    def getLvl(self):
        return self.value["lvl"]

    def getDescription(self):
        return self.value["description"]

    def getReaction(self):
        return self.value["reaction"]

    def getDamage(self):
        return self.value["damage"]

    def getDefense(self):
        return self.value["defense"]

    def getClass(self):
        return self.value["class"]

    def getPrice(self):
        return self.value["price"]

    def getStats(self):
        return self.value["stats"]

    def getValue(self):
        return self.value["value"]

    def getType(self):
        return self.value["type"]

    def getTypeOfEquipment(self):
        return self.value["typeOfEquipment"]

    def getTypeOfArmor(self):
        return self.value["typeOfArmor"]

    def reactionToConsumable(self, reaction):
        if reaction == Item.poissonCru.getReaction():
            return Item.poissonCru
        elif reaction == Item.painChaud.getReaction():
            return Item.painChaud
        elif reaction == Item.potionHeal.getReaction():
            return Item.potionHeal
