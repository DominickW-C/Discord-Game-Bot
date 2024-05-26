import random

#rps list 
RPSchoices = ["rock", "paper", "scissors"]

#logic for RPS
def rps(message):
     message = message.lstrip("!")
     botChoice = RPSchoices[random.randint(0,2)]

     if botChoice == message:
          return f"I picked: {botChoice} \nTie!"
     
     elif message == "rock":
          if botChoice == "paper":
               return f"I picked: {botChoice} \nI Win!"
          elif botChoice == "scissors":
               return f"I picked: {botChoice} \nYou Win!"
          
     elif message == "paper":
          if botChoice == "rock":
               return f"I picked: {botChoice} \nYou Win!"
          elif botChoice == "scissors":
               return f"I picked: {botChoice} \nI Win!"
          
     elif message == "scissors":
          if botChoice == "paper":
               return f"I picked: {botChoice} \nYou Win!"
          elif botChoice == "rock":
               return f"I picked: {botChoice} \nI Win!"
     else: 
          return "invalid input, please put: \n!rock \n!paper \n!scissors"