import random

import gamedev.level as lv
import gamedev.item as it

"""
Creation du personage principal par les utilisateurs du serveur
Mise en place d'un systeme de classe (Mage, archer, guerrier ) modifiant les attributs de base du personage
Definition des paramètres du personnage (Nom, PV, Defense, Attaque ect...)
Le caractère principale est un personnage de base plus développé (heritage classe personnage)
Le personnage est defini par les utilisateurs du serveur contrairement aux personnages secondaires / mob

"""


class Mob(object):

    def __init__(self, name, maxHp, hp, attack, defense, initiative, lvl):
        self.__name = name
        self.__maxHp = maxHp
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__initiative = initiative
        self.__lvl = lvl

    # -----------------------------------------------------------------------
    # GETTERS & SETTERS
    # -----------------------------------------------------------------------
    def getName(self):
        return self.__name

    def getMaxHp(self):
        return self.__maxHp

    def getHp(self):
        return self.__hp

    def getAttack(self):
        return self.__attack

    def getDefense(self):
        return self.__defense

    def getInitiative(self):
        if isinstance(self.__initiative, int):
            return self.__initiative

    def getLvl(self):
        if isinstance(self.__lvl, lv.Level):
            return self.__lvl

    def setMaxHp(self, maxHp):
        if isinstance(maxHp, int):
            self.__maxHp = maxHp

    def setHp(self, hp):
        if isinstance(hp, int):
            if 0 >= hp:
                self.__hp = 0
            elif hp >= self.getMaxHp():
                self.__hp = self.getMaxHp()
            else:
                self.__hp = hp

    def setAttack(self, attack):
        if isinstance(attack, int):
            self.__attack = attack

    def setDefense(self, defense):
        if isinstance(defense, int):
            self.__defense = defense

    def setInitiative(self, initiative):
        self.__initiative = initiative

    def setLvl(self, lvl):
        self.__lvl = lvl

    def setName(self, name):
        self.__name = name


class Character(Mob):
    def __init__(self, maxHp, hp, attack, defense, initiative, gold, xp):
        super().__init__("", maxHp, hp, attack, defense, initiative, lv.Level.level1)
        self.__inventory = []  # inventory list
        self.__equipmentInventory = [None, None, None, None, None]
        self.__gold = gold
        self.__xp = xp
        self.__class = None
        self.__spells = []
        self.__dodge = 0

    # -----------------------------------------------------------------------
    # GETTERS & SETTERS
    # -----------------------------------------------------------------------

    def getInventory(self):
        return self.__inventory

    def getEquipmentInventory(self):
        return self.__equipmentInventory

    def getGold(self):
        return self.__gold

    def getXp(self):
        return self.__xp

    def getSpells(self):
        return self.__spells

    def getClass(self):
        return self.__class

    def setInventory(self, inventory):
        self.__inventory = inventory

    def setEquipmentInventory(self, equipmentInventory):
        self.__equipmentInventory = equipmentInventory

    def setGold(self, gold):
        if isinstance(gold, int):
            self.__gold = gold

    def setXp(self, xp):
        if isinstance(xp, int):
            self.__xp = xp

    def setSpells(self, spells):
        self.__spells = spells

    def setClass(self, Class):
        self.__class = Class

    def getDodge(self):
        return self.__dodge

    def setDodge(self, value):
        self.__dodge=value

    # -----------------------------------------------------------------------
    # LOCAL FUNCTIONS
    # -----------------------------------------------------------------------

    def heal(self, amount):

        newAmount = self.getHp() + amount
        hpMax = self.getMaxHp()
        if newAmount <= hpMax:
            self.setHp(newAmount)
        else:
            self.setHp(hpMax)

    def maxHeal(self):
        self.setHp(self.getMaxHp())

    '''
    Give golds to player
    @:param amount: (int) the amount of gold
    '''

    def addGold(self, amount):
        self.setGold(self.getGold() + amount)

    '''
       Player spends golds
       @:param amount: (int) the amount of gold
       '''

    def spendGold(self, amount):
        self.setGold(self.getGold() - amount)

    def addXp(self, amount):
        val = amount + self.getXp() - self.getLvl().getXpNeeded()
        if val >= 0:
            while val >= 0:
                self.setLvl(self.getLvl().nextLevel())
                self.addCharacteristics()
                self.addSpells()
                self.setXp(val)
                val = val - self.getLvl().getXpNeeded()
        else:
            self.setXp(self.getXp() + amount)

    def addCharacteristics(self):       # a chaque levelUp, chaque classe gagnera ces caracteristiques
                                        # dans lordre resistance, attaque, pourcentage d'esquive.
        namePlayerClass = self.getClass().getName()

        if namePlayerClass == "archer":
            characList = [4, 2, 1]  # prev [5, 2, 1]
        elif namePlayerClass == "mage":
            characList = [2, 6, 1]  # prev [2, 8, 1]
        elif namePlayerClass == "guerrier":
            characList = [6, 4, 1]  # prev [8, 5, 1]

        self.setDefense(self.getDefense() + characList[0])
        self.setAttack(self.getAttack() + characList[1])
        self.setDodge(self.getDodge() + characList[2])

    def hasDodge(self):
        return random.randint(1, 100) <= self.getDodge()

    def useConsumable(self, consumable):
        if isinstance(consumable, it.Item) and consumable.getType() == "consumable":
            if consumable in self.getInventory():
                if consumable.getStats() == "hp":
                    if self.getHp() is not self.getMaxHp():  # pour proposer la liste des consomables, important de verifier avant que pv<hpmax
                        self.heal(consumable.getValue())
                        self.getInventory().remove(consumable)
                    return
                elif consumable.getStats() == "gold":
                    self.addGold(consumable.getValue())
                elif consumable.getStats() == "xp":
                    self.addXp(consumable.getValue())
                self.getInventory().remove(consumable)

    '''
    display the inventory
    '''

    def displayInventory(self):
        length = len(self.getInventory())
        print("[", end="")
        for i in range(length - 1):
            print(self.getInventory()[i].getName(), ";", end="", sep="")
        if length != 0:
            print(self.getInventory()[length - 1].getName(), end="")
        print("]")

    def displayEquipmentInventory(self):
        length = len(self.getEquipmentInventory())
        print("[", end="")
        for i in range(length - 1):
            if self.getEquipmentInventory()[i] is not None:
                print(self.getEquipmentInventory()[i].getName(), ";", end="", sep="")
            else:
                print(None, ";", end="", sep="")
        if length != 0:
            if self.getEquipmentInventory()[i] is not None:
                print(self.getEquipmentInventory()[length - 1].getName(), end="")
            else:
                print(None, end="")
        print("]")

    def displayPlayer(self):
        print("MaxHp     : ", self.getMaxHp())
        print("Hp         : ", self.getHp())
        print("Attack     : ", self.getAttack())
        print("Defense    : ", self.getDefense())
        print("Initiative : ", self.getInitiative())
        print("Gold       : ", self.getGold())
        print("Xp         : ", self.getXp())
        print("Level      : ", self.getLvl().getValue())
        print("Inventory  : ", end=" ")
        self.displayInventory()
        print("EquipmentInventory  : ", end=" ")
        self.displayEquipmentInventory()
        if self.getClass() is not None:
            print("Class      : ", self.getClass().getName())
        else:
            print("Class      : None")
        print("Spells     : ", self.getSpells())
        print("DodgePoint : ", self.getDodge())
    '''
    equip an equipment
    @:param : equipment, the equipment
    '''

    def Equip(self, equipment):
        if self.getLvl().getValue() >= it.Item.getLvl(equipment) and (
                self.getClass().getName() == it.Item.getClass(equipment) or it.Item.getClass(
            equipment) == "any"):

            typeOfEquipment = equipment.getTypeOfEquipment()

            if typeOfEquipment == "weapon":
                self.updateAttack(equipment)
                self.getEquipmentInventory()[0] = equipment
                return
            elif typeOfEquipment == "armor":

                typeOfArmor = equipment.getTypeOfArmor()

                if typeOfArmor == "helmet":
                    ind = 1
                elif typeOfArmor == "chestplate":
                    ind = 2
                elif typeOfArmor == "leggings":
                    ind = 3
                elif typeOfArmor == "boots":
                    ind = 4
                self.updateDefense(equipment, ind)
                self.getEquipmentInventory()[ind] = equipment
                return

    def UpdateClass(self):
        self.addSpells()
        self.setDodgePercent()
        self.addCharacteristics()

    def setDodgePercent(self):
        classPercent = self.getClass().getDodgePercent()
        self.setDodge(classPercent)

    def addSpells(self):
        lvl = self.getLvl()
        spells = self.getSpells()
        spellsOfClasses = self.getClass().getSpells()
        if lvl == lv.Level.level1:
            spells.append(spellsOfClasses[0])
        elif lvl == lv.Level.level5:
            spells.append(spellsOfClasses[1])
        #elif lvl == lv.Level.level10:          # need to develop more features
        #    spells.append(spellsOfClasses[2])

    def addInventory(self, item):
        if isinstance(item, it.Item) and item.getType() != "equipment":
            self.getInventory().append(item)
        elif isinstance(item, it.Item) and item.getType() == "equipment":
            self.Equip(item)

    def updateDefense(self, equipment, ind):
        if isinstance(equipment, it.Item) and isinstance(ind, int) and 1 <= ind <= 4:
            defense = self.getDefense()
            equipInventory = self.getEquipmentInventory()
            defenseOfNewEquipment = equipment.getDefense()

            if equipInventory[ind] is None:
                self.setDefense(defense + defenseOfNewEquipment)
            else:
                defenseOfOldEquipment = equipInventory[ind].getDefense()
                newDefense = defense - defenseOfOldEquipment + defenseOfNewEquipment
                self.setDefense(newDefense)

    def updateAttack(self, equipment):
        if isinstance(equipment, it.Item):
            attack = self.getAttack()
            equipInventory = self.getEquipmentInventory()
            damageOfNewEquipment = equipment.getDamage()

            if equipInventory[0] is None:
                self.setAttack(attack + damageOfNewEquipment)
            else:
                damageOfOldEquipment = equipInventory[0].getDamage()
                newDamage = attack - damageOfOldEquipment + damageOfNewEquipment
                self.setAttack(newDamage)

    def getConsumable(self):
        res = []
        inventory = self.getInventory()
        for conso in inventory:
            if isinstance(conso, it.Item):
                if conso.getType() == "consumable":
                    if conso not in res:
                        res.append(conso)
        return res
