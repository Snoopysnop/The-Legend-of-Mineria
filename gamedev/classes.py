from enum import Enum
import gamedev.attack as att


class Classes(Enum):

    Archer = {"Name": "archer", "dodgePercent": 40, "spellsList": [att.Attack.arrow, att.Attack.multiArrow]}
    Guerrier = {"Name": "guerrier", "dodgePercent": 10, "spellsList": [att.Attack.sword, att.Attack.spinningSword]}
    Mage = {"Name": "mage", "dodgePercent": 25, "spellsList": [att.Attack.fireball, att.Attack.iceShard]}

    def getName(self):
        return self.value["Name"]

    def getSpells(self):
        return self.value["spellsList"]

    def getDodgePercent(self):
        return self.value["dodgePercent"]
