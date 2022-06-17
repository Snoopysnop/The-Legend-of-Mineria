from enum import Enum


class Attack(Enum):

    fireball = {"damage": 30, "name": "Boule de feu", "description": "Une boule de feu impossible à bloquer", "reaction": "🔥", "spellType": "monoSpell"}
    #healing = {"damage": 100, "name": "Soin angelique", "description": "la foudre s'abat ", "reaction": "", "spellType": "monoSpell"}
    iceShard = {"damage": 20, "name": "Eclat de glace", "description": "Un eclat de glace stylé", "reaction": "❄️", "spellType": "multiSpell"}


    sword = {"damage": 25, "name": "Coup d'épée", "description": "Une coup d'épée impossible à esquiver", "reaction": "🗡️", "spellType": "monoSpell"}
    #bigSword = {"damage": 60, "name": "Gros coup d'épée", "description": "un gros coup d'eppe s'abat ", "reaction": "", "spellType": "monoSpell"}
    spinningSword = {"damage": 17, "name": "epee divine", "description": "lepee tourbillonne et pourfend les adversaires en zone ", "reaction": "⚔", "spellType": "multiSpell"}

    arrow = {"damage": 18, "name": "Tir à l'arc", "description": "Une flèche infligeant de lourds dégâts", "reaction": "🏹", "spellType": "monoSpell"}
    #bigArrow = {"damage": 60, "name": "Grosse fleche", "description": "une grosse fleche stylée ", "reaction": "", "spellType": "monoSpell"}
    multiArrow = {"damage": 13, "name": "fleches multiples", "description": "une pluie de fleches s'abat sur les adversaires ", "reaction": "🎯", "spellType": "multiSpell"}

    def getDamage(self):
        return self.value["damage"]

    def getName(self):
        return self.value["name"]

    def getDescription(self):
        return self.value["description"]

    def getReaction(self):
        return self.value["reaction"]

    def getSpellType(self):
        return self.value["spellType"]

    def reactionToSpell(self, reaction):

        if reaction ==  Attack.fireball.getReaction():
            return Attack.fireball
        elif reaction == Attack.iceShard.getReaction():
            return Attack.iceShard
        elif reaction ==  Attack.arrow.getReaction():
            return Attack.arrow
        elif reaction ==  Attack.multiArrow.getReaction():
            return Attack.multiArrow
        elif reaction == Attack.sword.getReaction():
            return Attack.sword
        elif reaction ==  Attack.spinningSword.getReaction():
            return Attack.spinningSword
