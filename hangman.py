import random
import os
import sys

localFileName = "wordList.txt"
fileName = os.path.join(sys.path[0], localFileName)
f = open(fileName)
fileLines = f.readlines()

def readWordList():
    wordList = []
    for line in open(fileName):
        wordList.append(line.strip())
    return wordList

def hangmanGameLoop():
    hangmanPictures =  {
        0: 
    """
    |________
    |
    |
    |
    |
    |________
    """,
        1:
    """
    |________
    |   |
    |
    |
    |
    |________
    """,
        2:
    """
    |________
    |   |
    |   O
    |
    |
    |________
    """,
        3:
    """
    |________
    |   |
    |   O
    |   |
    |
    |________
    """,
        4:
    """
    |________
    |   |
    |   O
    |   |
    |   /\\
    |________
    """,
        5:
    """
    |________
    |   |
    |  _O_
    |   |
    |   /\\
    |________
    """,
    }


    word = random.choice(readWordList())
    guessCount = 0
    guessedWord = ["_"] * len(word)
    missedLetters = []
    missedCount = 0

    loseAmount = 6

    while True:
        guessCount += 1
        guessCharacter = input("Guess a letter: ")
        correct = False
        for index, c in enumerate(word):
            if c == guessCharacter:
                guessedWord[index] = c
                correct = True
        if not correct:
            missedLetters.append(guessCharacter)
            missedCount += 1
            print("Incorrect!")
            if missedCount >= loseAmount:
                print("You lose")
                print("The word was " + word)
                break
        else:
            print("Correct!")
            if "_" not in guessedWord:
                print("You win")
                print("The word was " + word)
                break
        print(" ".join(guessedWord))
        print("Missed Letters: " + ",".join(missedLetters))
        print(hangmanPictures[missedCount])

def wordListChanging():

    wordList = readWordList()
    seeWordList = input("Would you like to see the word list? (type 'yes' to see)")
    if seeWordList == "yes":
        for index, i in enumerate(wordList):
            print(str(index) + ". " + i)
    editWordList = input("Would you like to edit the word list? (type 'yes' to see)")
    if editWordList == "yes":
        editSetting = input("Would you like to delete, edit or add a word")
        f = open(fileName)
        fileLines = f.readlines()
        if editSetting == "edit":
            while True:
                wordIndex = input("Enter the index of the word you would like to edit")
                if wordIndex.isdigit():
                    wordIndex = int(wordIndex)
                    if 0 <= wordIndex < len(wordList):
                        break
                print("Please enter a valid integer")
            newWord = input("Enter a new word")
            fileLines[wordIndex] = newWord

        if editSetting == "delete":
            while True:
                wordIndex = input("Enter the index of the word you would like to delete")
                if wordIndex.isdigit() and 0 <= wordIndex < len(wordList):
                    wordIndex = int(wordIndex)
                    if 0 <= wordIndex < len(wordList):
                        break
                print("Please enter a valid integer")
            fileLines.pop(wordIndex)

        if editSetting == "add":
            newWord = input("Enter a new word")
            fileLines.append(newWord)

    f = open(fileName, "w")

    f.write("\n".join([line.strip() for line in fileLines]))
    f.close()

if __name__ == "__main__":
    print("This is the wrong file, please run 'mainGame.py'")