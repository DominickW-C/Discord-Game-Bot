#Want to implement:
#something to block you from guessing the same letter twice

import random
import os

#this causes the txt to reset, find a way that doesn't do that
cache = open("hangmanCache.txt", "r")

#takes from text file and saves it to var
storeRead = []
for line in cache:
    storeRead.append(line.rstrip())

#refreshes the text document and puts it in write mode
def reopen():
    global cache
    os.remove("hangmanCache.txt")
    cache = open("hangmanCache.txt", "w")

#vars needed 
pickedWord = storeRead[0]
currentWord = storeRead[1]
lettersGuessed = storeRead[2]
rightWrong = ""
chances = 0

#creates/refreshes the game
def create():
    global pickedWord, currentWord, lettersGuessed, chances
    
    #resets file
    reopen()
    chances = 0

    #chooses random word
    wordsFile = open("words.txt", "r")
    wordsList = []
    for line in wordsFile:
        wordsList.append(line.rstrip())
    pickedWord = wordsList[random.randint(0, len(wordsList) - 1)]
    
    #set current word to blank, and empties letters guessed
    currentWord = ("-" * len(pickedWord))
    lettersGuessed = "guessed: "
    
    #writes to text doc and closes
    cache.write(f'''{pickedWord}\n{currentWord}\n{lettersGuessed}''')
    cache.close()

#changes the letter to a -, recursively calls itself to fill in duplicates
def change(letter):
    global pickedWord, currentWord, lettersGuessed

    #try and except for if there is no duplicate it won't throw an error
    try:
        indexNum = list(pickedWord).index(letter)
        
        #contructs it as a list, changes, and recontructs as a string
        currentWordList = list(currentWord)
        currentWordList[indexNum] = letter
        currentWord = ""
        for let in currentWordList:
            currentWord += let

        pickedWordList = list(pickedWord)
        pickedWordList[indexNum] = "-"
        pickedWord = ""
        for let in pickedWordList:
            pickedWord += let

        change(letter)
        
    except:
        pass

#checks your guess
def guess(letter):
    global pickedWord, currentWord, lettersGuessed, rightWrong, chances

    lettersGuessed += letter 
    pickedWordList = list(pickedWord)
    reopen()

    #checks if letter was in word list
    if letter in pickedWordList:
        change(letter)
        rightWrong = "Letter was in the word!"
    else:
        rightWrong = "Letter was not in the word!"
        chances += 1

    #writes to text doc
    cache.write(f'''{pickedWord}\n{currentWord}\n{lettersGuessed}''')
    cache.close()

def hangmanOutput():
    global chances

    #makes sure that the text doc saves and is readable
    cache.close()
    readCache = open("hangmanCache.txt", "r")

    #saves the data so it can be outputted in discord
    txtData = []
    for line in readCache:
        txtData.append(line.rstrip())

    #checks if you can still play or not
    if chances == 6:
        out = f"Game Over!\n\n{man()}"
        create()
        chances = 0 
        return out
    else:
        return f'''{rightWrong}\n\ncurrent word:\n{txtData[1]}\n\n{txtData[2]}\n\n{man()}'''

#man art
def man():
    if chances == 0:
        return '''
            \_ \_ \_ \_
            |         |
            |
            |
            |
            |
            |
            |
          -----
    '''
    elif chances == 1:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |    
            |    
            |
            |
        -----
    '''
    elif chances == 2:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |         |
            |         |
            |         |
            |
        -----
    '''
    elif chances == 3:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |         |   /
            |         |  /
            |         |
            |
        -----
    '''
    elif chances == 4:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |     \   |   /
            |      \  |  /
            |          |
            |
        -----
    '''
    elif chances == 5:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |      \  |  /
            |       \ | /
            |         |
            |       /
        -----
    '''
    elif chances == 6:
            return '''
            \_ \_ \_ \_
            |         |
            |        ---
            |       |     |
            |        ---
            |      \  |  /
            |       \ | /
            |         |
            |       /   \  
        -----
    '''
    