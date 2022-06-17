import requests
import json
import time

class DiscordMessage:
    
    def __init__(self, user):
        self.user = user

    def sendMessage(self, channelID, message):
        time.sleep(0.1)
        res = requests.post("https://discord.com/api/channels/" + str(channelID) + "/messages",
            data =  json.dumps({"content": message}),
            headers = {"Authorization": self.user,
            "Content-Type":"application/json"})
        return int(res.json()["id"])

    def editMessage(self, channelID, messageID, message):
        time.sleep(0.1)
        requests.patch("https://discord.com/api/channels/" + str(channelID) + "/messages/" + str(messageID),
            data =  json.dumps({"content": message}),
            headers = {"Authorization": self.user,
            "Content-Type":"application/json"})
 
    def getReactions(self, channelID, messageID):
        time.sleep(0.1)
        res = requests.get("https://discord.com/api/v9/channels/" + str(channelID) + "/messages/" + str(messageID),
                   headers = {"Authorization": self.user})
        try:
            return json.loads(res.text)["reactions"]
        except:
            return {}
    
    def sendReaction(self, channelID, messageID, reaction):
        time.sleep(0.1)
        requests.put("https://discord.com/api/v9/channels/" + str(channelID) + "/messages/" + str(messageID) + "/reactions/" + reaction + "/%40me",
                      headers = {"Authorization": self.user})
    
    def sendReactions(self, channelID, messageID, reactions):
        for reaction in reactions:
            self.sendReaction(channelID, messageID, reaction)
        
    def removeReaction(self, channelID, messageID, reaction):
        time.sleep(0.1)
        requests.delete("https://discord.com/api/v9/channels/" + str(channelID) + "/messages/" + str(messageID) + "/reactions/" + reaction,
                      headers = {"Authorization": self.user})
        
    def removeReactions(self, channelID, messageID):
        reactions = self.getReactions(channelID, messageID)
        for reaction in reactions:
            self.removeReaction(channelID, messageID, reaction["emoji"]["name"])
    
    def sendEmbed(self, channelID, embed):
        time.sleep(0.1)
        res = requests.post("https://discord.com/api/channels/" + str(channelID) + "/messages",
            headers = {"Authorization": self.user,
            "Content-Type":"application/json"},
            data = json.dumps(embed))
        return int(res.json()["id"])
    
    
        
    def editEmbed(self, channelID, messageID, embed):
        time.sleep(0.1)
        requests.patch("https://discord.com/api/channels/" + str(channelID) + "/messages/" + str(messageID),
            data =  json.dumps(embed),
            headers = {"Authorization": self.user,
            "Content-Type":"application/json"})
