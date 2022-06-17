import gamedev.character as ch
import gamedev.attack as att


class Combat(object):
    def __init__(self, player, listEnemy):
        self.__player = player
        self.__listEnemy = listEnemy
        self.__playerDead = False
        self.__fightEnd = False
        self.__order = self.order()  # monster starts
        self.__selectEnemy = self.getListEnemy()[0]

    # -----------------------------------------------------------------------
    # GETTERS & SETTERS
    # -----------------------------------------------------------------------

    def getPlayer(self):
        return self.__player

    def getListEnemy(self):
        return self.__listEnemy

    def getPlayerDead(self):
        return self.__playerDead

    def getFightEnd(self):
        return self.__fightEnd

    def getOrder(self):
        return self.__order

    def getSelectEnemy(self):
        return self.__selectEnemy

    def setPlayer(self, player):
        self.__player = player

    def setOrder(self, order):
        self.__order = order

    def setListEnemy(self, listEnemy):
        self.__listEnemy = listEnemy

    def setPlayerDead(self, playerDead):
        self.__playerDead = playerDead

    def setFightEnd(self, fightEnd):
        self.__fightEnd = fightEnd

    def setSelectEnemy(self, selectEnemy):
        self.__selectEnemy = selectEnemy

    # -----------------------------------------------------------------------
    # LOCAL FUNCTIONS
    # -----------------------------------------------------------------------

    def isMobDead(self, monster):
        return (monster.getHp() <= 0) & (monster in self.getListEnemy())

    def isPlayerDead(self):
        if self.getPlayer().getHp() <= 0:
            self.setPlayerDead(True)
            return True
        return False

    def areAllMobDead(self):
        return len(self.getListEnemy()) == 0

    def fightIsEnd(self):
        if self.areAllMobDead() or self.isPlayerDead():
            self.setFightEnd(True)
            return True
        return False

    def damage(self, amount):
        if isinstance(amount, int):
            damages = amount - self.getPlayer().getDefense()
            if damages >= 0:
                self.getPlayer().setHp(self.getPlayer().getHp() - damages)

    def order(self):
        return self.getPlayer().getInitiative() >= self.getListEnemy()[0].getInitiative()

    def attackAllEnemies(self, attack):
        enemy = self.getListEnemy()
        for monster in enemy:
            self.attackOneEnemy(attack, monster)

    def attackOneEnemy(self, attack, monster):

        amount = att.Attack.getDamage(attack) + self.getPlayer().getAttack()
        damages = amount - monster.getDefense()
        if damages >= 0:
            monster.setHp(monster.getHp() - damages)

    def updateRoundOfPlay(self, attack):

        if isinstance(attack, att.Attack):
            typeAttack = att.Attack.getSpellType(attack)
            selectedEnemy = self.getSelectEnemy()
            firstMonster = self.getListEnemy()[0]

            if self.getOrder():  # player starts
                if typeAttack == "multiSpell":  # player plays
                    self.attackAllEnemies(attack)
                else:
                    self.attackOneEnemy(attack, selectedEnemy)
                if not self.isMobDead(firstMonster):  # first mob plays
                    if not self.getPlayer().hasDodge():
                        self.damage(firstMonster.getAttack())
            else:  # mob starts
                if not self.getPlayer().hasDodge():  # first mob plays
                    self.damage(firstMonster.getAttack())
                if not self.isPlayerDead():  # player plays
                    if typeAttack == "multiSpell":
                        self.attackAllEnemies(attack)
                    else:
                        self.attackOneEnemy(attack, selectedEnemy)

            retList = []
            for monster in self.getListEnemy():  # rest of monsters plays
                if not self.isMobDead(monster):
                    retList.append(monster)
                    if not(monster == self.getListEnemy()[0]) and not(self.getPlayer().hasDodge()):
                        self.damage(monster.getAttack())
            self.setListEnemy(retList)

            if len(self.getListEnemy()) == 1:  # case where there is only 1 mob left and player know that he has to
                self.setSelectEnemy(self.getListEnemy()[0])  # attack him then selectEnemy won't be update in event.py
            self.fightIsEnd()
            self.isPlayerDead()

    def reactionMobToStr(self, reaction):  # select mob that we will hit
        if isinstance(reaction, str):

            if reaction == "1️⃣":
                self.setSelectEnemy(self.getListEnemy()[0])
            if reaction == "2️⃣":
                self.setSelectEnemy(self.getListEnemy()[1])
            if reaction == "3️⃣":
                self.setSelectEnemy(self.getListEnemy()[2])
            if reaction == "4️⃣":
                self.setSelectEnemy(self.getListEnemy()[3])
            if reaction == "5️⃣":
                self.setSelectEnemy(self.getListEnemy()[4])
            if reaction == "6️⃣":
                self.setSelectEnemy(self.getListEnemy()[5])
            if reaction == "7️⃣":
                self.setSelectEnemy(self.getListEnemy()[6])
            if reaction == "8️⃣":
                self.setSelectEnemy(self.getListEnemy()[7])
            if reaction == "9️⃣":
                self.setSelectEnemy(self.getListEnemy()[8])
