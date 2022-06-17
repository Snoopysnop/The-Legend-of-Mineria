from Bot.DiscordMessage import *
from gamedev.item import *

class EmbedBuilder():
    
    
    def __init__(self, event, character):
        self.embed = {}
        if("title" in event):
            self.embed["content"] =  event["title"]
            
        elif("title_special" in event):
    
            title_special = event["title_special"]
            title = ""
            for word in title_special.split(" "):
                if "\n" in word:
                    title += "\n"  
                try:
                    title += str(eval(word)) + " "
                except:
                    title += word + " "
            self.embed["content"] = title
        
        fields = []
        
        if("choices" in event):
            for choice in event["choices"]:
                temp = {}
                temp["name"] = choice["Reaction"] + " " + choice["name"]
                temp["value"] = choice["value"]
                fields.append(temp)
                
            self.embed["embeds"] = [{"image": {"url": event["image"]}, "fields":fields}]
            
        else:
            self.embed["embeds"] = [{"image": {"url": event["image"]}}]
        
        
