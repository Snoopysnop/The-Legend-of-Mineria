from enum import Enum


class Level(Enum):
    level1 = {"value": 1, "xpNeeded": 50}
    level2 = {"value": 2, "xpNeeded": 75}
    level3 = {"value": 3, "xpNeeded": 100}
    level4 = {"value": 4, "xpNeeded": 150}
    level5 = {"value": 5, "xpNeeded": 225}
    level6 = {"value": 6, "xpNeeded": 325}
    level7 = {"value": 7, "xpNeeded": 450}
    level8 = {"value": 8, "xpNeeded": 600}
    level9 = {"value": 9, "xpNeeded": 800}
    level10 = {"value": 10, "xpNeeded": 1100}
    level11 = {"value": 11, "xpNeeded": 1500}
    level12 = {"value": 12, "xpNeeded": 2000}
    level13 = {"value": 13, "xpNeeded": 3000}
    level14 = {"value": 14, "xpNeeded": 5000}
    level15 = {"value": 15, "xpNeeded": 10000}
    level16 = {"value": 16, "xpNeeded": 20000}
    level17 = {"value": 17, "xpNeeded": 35000}
    level18 = {"value": 18, "xpNeeded": 50000}
    level19 = {"value": 19, "xpNeeded": 75000}
    level20 = {"value": 20, "xpNeeded": 100000}

    def getValue(self):
        return self.value["value"]

    def getXpNeeded(self):
        return self.value["xpNeeded"]

    def nextLevel(self):
        if isinstance(self, Level):
            val = self.getValue()
            if val != 20:
                listOfLevels = list(Level)
                return listOfLevels[val]
