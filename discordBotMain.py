#libraries 
import discord
from rockPaperScissors import rps, RPSchoices
from rollBot import roll
from hangman import *

#personal token and link to add to a server
token = ""
link = "https://discord.com/oauth2/authorize?client_id=1242843422436626472&permissions=1084479764544&scope=bot"

#help message 
help = '''
Hello! I am a game bot with the abilities to play RPS, and roll a dice (more to come in the future!)
Here is a list of commands that I am currently able to do:\n
     \- !(rock, paper, scissors) will play a game of rock paper scissors
     \- !(any number) will roll a dice as large as any number that you give it
     \- !reset will reset the hangman game or make a new game
     \- !(single letter) will guess that letter for the hangman game
'''

#bot setup
intents = discord.Intents.default() 
intents.message_content = True
client = discord.Client(intents = intents)

#when the bot starts
@client.event
async def on_ready():
     print("bot is up and running")
     
#when a message is sent
@client.event
async def on_message(message):
     #checks if it is a messager meant for the bot
     if message.content.startswith("!") and str(message.author.bot) == "False":
          msg = message.content.lstrip("!")
          
          #checks if digit
          try:
               msg = int(msg)
               await message.channel.send(roll(msg))
          except:
               #checks what word was inputted
               if msg in RPSchoices:
                    await message.channel.send(rps(message.content))
               
               if msg == "help":
                    await message.channel.send(help)

               if msg == "reset":
                    create()
                    await message.channel.send(hangmanOutput())
                    
               if len(msg) == 1:
                    guess(msg.lower())
                    await message.channel.send(hangmanOutput())

#runs the bot
client.run(token)