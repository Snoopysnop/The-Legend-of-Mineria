from Bot.DiscordMessage import *
from Bot.Embed import *
from datetime import datetime, timedelta
from gamedev.character import *
from gamedev.combat import *
from gamedev.attack import *
from gamedev.classes import *
from gamedev.item import *

import random
import copy

class Event ():
    
    cheatmode = False
    current_respawn = "0"
    quests_completed = []
    character = Character(200, 200, 0, 0, 3, 0, 0)

    fight = None
    targetting = False
    timeline_index = 0
        
    def __init__(self, key):  
                
        def applySpecifities(self, event):
            for spec in event["specificities"]:
                if(spec == "respawn_point"):
                    Event.current_respawn = self.key
                if(spec == "healing_point"):
                    Event.character.maxHeal()    
                if("gold" in spec):
                    Event.character.addGold(spec["gold"])   
        
        self.key = key
        event = copy.deepcopy(Event.events[self.key])
        

        if("timeline" in event):
            if(event["timeline"][Event.timeline_index] != "None"):
                
                timeline_next = event["timeline"][Event.timeline_index]
                if(type(timeline_next) == dict):
                    r = random.randrange(100)
                    key_list = list(timeline_next.keys())
                    for key in key_list:
                        if(0<=r<=timeline_next[key]):
                            self.key = key
                            break
                        r = r-timeline_next[key]
                
                else:
                    self.key = timeline_next
                    
                event = copy.deepcopy(Event.events[self.key])
            Event.timeline_index += 1  
        
        if("choices" in event):
            choices_to_remove = []
            for i in range(len(event["choices"])):
                choice = event["choices"][i]
                if "default" in choice:
                    choice_key = self.select_choice(choice)
                    if(choice[choice_key] == "None"):
                        choices_to_remove.append(choice)
                    else:
                        event["choices"][i] = choice[choice_key]
                        
            for choice in choices_to_remove:
                event["choices"].remove(choice)
        
        if("specificities" in event):
            applySpecifities(self, event)
            
        if("mobs" in event):
            if(Event.fight == None):
                adversaires = []
                for mob in event["mobs"]:
                    adversaires.append(Mob(mob["name"], mob["max_hp"], mob["hp"], mob["attack"], mob["defense"], mob["initiative"], mob["lvl"]))
                Event.fight = Combat(Event.character, adversaires)
                Event.fight.order()

            if(not(Event.targetting)):
                self.event = event
                targetting_result = self.set_targetting(True)
                
                self.key = targetting_result["key"]
                event = targetting_result["event"]
                
            if(Event.targetting):
                choices  = []
                for spell in Event.character.getSpells():
                    choices.append({"name":f"{spell.getName()}", "value":spell.getDescription(), "Reaction":spell.getReaction()})
                for item in Event.character.getConsumable():
                    choices.append({"name":f"{item.getName()}", "value":f"{item.getDescription()} \n{item.getValue()} ❤️", "Reaction":item.getReaction()})
                event["choices"] = choices
                
                event["title"] = event["title"] + f"\nPV Joueur : {Event.character.getHp()} / {Event.character.getMaxHp()}"
                for mob in Event.fight.getListEnemy():
                    event["title"] = event["title"] + f"\nPV {mob.getName()} : {mob.getHp()} / {mob.getMaxHp()}"
                event["title"] = event["title"] + f"**\nVous ciblez {Event.fight.getSelectEnemy().getName()}**"
               
        self.event = event
        self.embed = EmbedBuilder(self.event, Event.character).embed
        self.send()

    def send(self):
        if(Event.messageID == None):
            Event.messageID = Event.user.sendEmbed(Event.channelID, self.embed)
            
        else:
            Event.user.editEmbed(Event.channelID, Event.messageID, self.embed)
            
        if("choices" in self.event):
            for choice in self.event["choices"]:
                time.sleep(0.1)
                Event.user.sendReaction(Event.channelID, Event.messageID, choice["Reaction"])
                
    def select_choice(self, choice):
        key_list = list(choice.keys())
        for key in key_list:
            if key in Event.quests_completed:
                return key
        return "default"
    
    def select_random_next(self, nexts):
        r = random.randrange(100)
        key_list = list(nexts.keys())
        for key in key_list:
            if(0<=r<nexts[key]):
                return key
            r = r-nexts[key]
            
    def set_targetting(self, starting):
        
        adversaires = Event.fight.getListEnemy()
        if(len(adversaires) == 1):
            Event.targetting = True
            if(not(starting)):
                return Event(self.key)
            else:
                return {"key":self.key, "event":self.event}
        
        else:
            Event.fight = Combat(Event.character, adversaires)
            reaction = ["1️⃣", "2️⃣", "3️⃣" , "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
            next_key = self.key
            key = "selector"
            
            choices = []
            adversaires = Event.fight.getListEnemy()
            for i in range (len(adversaires)):
                choices.append({"name":adversaires[i].getName(), "value":f"PV : {adversaires[i].getHp()} / {adversaires[i].getMaxHp()}", "next":next_key, "Reaction": reaction[i]})
            Event.events[key]["choices"] = choices
        
            Event.events[key]["image"] = self.event["image"]
            
            #title = f"{self.event['title']}\nQuel ennemi voulez-vous attaquer ?\nPlayer {Event.character.getHp()} / {Event.character.getMaxHp()}"
            title = f"Quel ennemi voulez-vous attaquer ?\nPV Joueur : {Event.character.getHp()} / {Event.character.getMaxHp()}"
            Event.events[key]["title"] = title 
            if(not(starting)):
                Event.targetting = True
                return Event(key)
            else:
                return {"key":key, "event":copy.deepcopy(Event.events[key])}
          
    def rewards(self, key):
        
        Event.events["rewards"]["title"] = f"PV Joueur : {Event.character.getHp()} / {Event.character.getMaxHp()}"
        
        Event.events["rewards"]["image"] = self.event["image"]
        Event.events["rewards"]["choices"][0]["next"] = key
        
        if("rewards" in self.event):
            Event.events["rewards"]["title"] += f"\nVoici vos récompenses :"
            rewards = self.event["rewards"]
            if("xp" in rewards):
                Event.events["rewards"]["title"] += f"\nExperience : {Event.character.getXp()} -> {Event.character.getXp() + rewards['xp']} / {Event.character.getLvl().getXpNeeded()} (niveau {Event.character.getLvl().getValue()})"
                Event.character.addXp(rewards["xp"])
                
                
            if("gold" in rewards):
                Event.events["rewards"]["title"] += f"\nOr 🪙 : {Event.character.getGold()} -> {Event.character.getGold() + rewards['gold']}"
                Event.character.addGold(rewards["gold"])   
        
            if("loots" in rewards):
                Event.events["rewards"]["title"] += "\n**Objets** :"
                loots = rewards["loots"]
                
                r = random.randrange(100)
                key_list = list(loots.keys())
                for key in key_list:
                    if(0<=r<loots[key]):
                        item = eval(key)
                        Event.character.addInventory(item)
                        Event.events["rewards"]["title"] += f"\n{item.getName()} : {item.getDescription()}"
                        
                    
        return Event("rewards")  
                    
    def getClasse(self, reaction):
        if(reaction == "🗡"):
            Event.character.setClass(Classes.Guerrier)
        elif(reaction == "🏹"):
            Event.character.setClass(Classes.Archer)
        elif(reaction == "🪄"):
            Event.character.setClass(Classes.Mage)
            
        Event.character.UpdateClass()
        
    def respawn(self):
        Event.fight = None
        Event.targetting = False
        Event.events["revive"]["choices"][0]["next"] = Event.current_respawn
        return Event("death")
    
    def update(self, reaction):
        Event.user.removeReactions(Event.channelID, Event.messageID)
        
        if("specificities" in self.event):
            for spec in self.event["specificities"]:
                if(spec == "death"):
                    return self.respawn()
                if("hp" in spec):
                    Event.character.heal(spec["hp"])
                    if(Event.character.getHp() <= 0):
                        return self.respawn()
        
        if(Event.fight != None and (not(Event.targetting) or self.key=="selector")):
            Event.fight.reactionMobToStr(reaction)
            Event.targetting = True
            if(self.key == "selector"):
                key = self.event["choices"][0]["next"]
            else:
                key = self.key
            return Event(key)
            
        if(Event.fight != None and Event.targetting and self.key != "selector" and  not("special_fight_event" in self.event)):
                
            if(Item.reactionToConsumable(None, reaction) != None):
                Event.character.useConsumable(Item.reactionToConsumable(None, reaction))
                Event.targetting = True
                return Event(self.key)
            
            elif(Attack.reactionToSpell(None, reaction) != None):
                Event.fight.updateRoundOfPlay(Attack.reactionToSpell(None, reaction))
                Event.targetting = False
               
                if(Event.fight.getFightEnd()):
                    Event.timeline_index = 0
                             
                    #le joueur a perdu
                    if(Event.fight.getPlayerDead()):
                        Event.fight = None
                        return self.respawn()
                    else:
                        #le joueur a gagné
                        Event.fight = None
                        
                        if(type(self.event["next"]) == dict):
                            key = self.select_random_next(self.event["next"])
                        else:
                            key = self.event["next"]
                        
                        Event.quests_completed.append(self.key)
                        return self.rewards(key)
                    
                else:

                    return self.set_targetting(False)
        
        else:
            Event.quests_completed.append(self.key)
            
            if(self.key == "6"):
                self.getClasse(reaction)
                
            for choice in self.event["choices"]:
                if(choice["Reaction"] == reaction):
                    
                    if(type(choice["next"]) == dict):
                        key = self.select_random_next(choice["next"])
                    else:
                        
                        if("required" in choice):
                            if("gold" in choice["required"]):
                                if(Event.character.getGold() < choice["required"]["gold"]):
                                    lastEmbed = self.embed["content"]
                                    self.embed["content"] = self.embed["content"] + "\n**Vous n'avez pas assez d'or**"
                                    self.send()
                                    self.embed["content"] = lastEmbed
                                    return self
                            
                            
                        key = choice["next"]
                    
                    
                    if("timer" in choice and not(Event.cheatmode)):
                        current_datetime = datetime.now()
                        finish_datetime = current_datetime + timedelta(seconds = choice["timer"])
                        finish_datetime_str = f"{finish_datetime.hour + 2}:{finish_datetime.minute}:{finish_datetime.second}"
                        
                        embeds  = [{"image": {"url": self.event["image"]}, "fields":[{"name":choice["name"], "value":choice["value"]}]}]
                        embed = {"content":f"{self.event['title']}\n**Suite à {finish_datetime_str}**", "embeds":embeds}
                        if(Event.messageID == None):
                            Event.messageID = Event.user.sendEmbed(Event.channelID, embed)
                        else:
                            Event.user.editEmbed(Event.channelID, Event.messageID, embed)
                    
                        time.sleep(choice["timer"])
                    
                    
                    if("rewards" in self.event):
                        return self.rewards(key)
                    
                    return Event(key)
                
        print("Erreur ?!")
        return self
