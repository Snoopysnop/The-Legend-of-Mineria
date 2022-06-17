from gamedev.event import *
from Bot.DiscordMessage import *
import discord
import mysql.connector


channelID = input()

with open("Bot/creds.json", "r", encoding="utf-8") as file:
    creds = json.load(file)

userID = creds["application"]["id"]
auth = creds["application"]["token"]

database_host = creds["database"]["host"]
database_user = creds["database"]["user"]
database_password = creds["database"]["password"]
database_name = creds["database"]["name"]



Event.user = DiscordMessage("Bot " + auth)
Event.channelID = channelID
Event.messageID = None
with open("gamedev/events.json", "r", encoding="utf-8") as file:
    Event.events = json.load(file)
Event.cheatmode = True
e = Event("0")

client = discord.Client()

def getRVOTE():

    rvote = -1
    mydb = mysql.connector.connect(
        host = database_host,
        user = database_user,
        password = database_password,
        database = database_name
    )

    global channelID
    cmd = "SELECT RVOTE FROM SERVERS WHERE CHANNELID=" + str(channelID)
    mycursor = mydb.cursor()
    mycursor.execute(cmd)
    for x in mycursor:
        rvote = x[0]

    
    return rvote

rvote = getRVOTE()
if(rvote == -1):
    exit()


@client.event
async def on_raw_reaction_add(reaction):
    global e
    
    if(reaction.message_id == Event.messageID and reaction.user_id != userID):
        reactions = Event.user.getReactions(Event.channelID, Event.messageID)
        
        global rvote
        for reaction_json in reactions:
            if(not(reaction_json["me"])):
                Event.user.removeReaction(Event.channelID, Event.messageID, reaction.emoji.name)
            elif(reaction_json["count"] == rvote+1):
                e = e.update(reaction_json["emoji"]["name"])
                rvote = getRVOTE()
                if(rvote == -1):
                    exit()

@client.event
async def on_raw_message_delete(message):
    global e
    if(message.message_id == Event.messageID):

        global rvote
        rvote = getRVOTE()
        if(rvote == -1):
            exit()
        Event.messageID = None
        e.send()

@client.event
async def on_raw_reaction_remove(reaction):
    if(reaction.message_id == Event.messageID and reaction.user_id == userID):
        Event.user.sendReaction(Event.channelID, Event.messageID, reaction.emoji.name)
        
        
@client.event
async def on_raw_reaction_clear(payload):
    global e
    
    if("choices" in e.event):
        for choice in e.event["choices"]:
            print(choice["Reaction"])
            time.sleep(0.1)
            Event.user.sendReaction(Event.channelID, Event.messageID, choice["Reaction"])

client.run(auth)
