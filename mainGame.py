import hangman
import connectfour 
import tictactoe

while True:
    while True:
        userChoice = input("Would you like to play a game (type 'game'), or change settings (type 'settings'), or quit the program (type 'quit')")
        if userChoice == "game":
            while True:
                gameChoice = input("What game would like to play (hangman, connectfour, tictactoe)")
                if gameChoice == "hangman":
                    hangman.hangmanGameLoop()
                    break
                if gameChoice == "connectfour":
                    connectfour.connectfourGameLoop()
                    break
                if gameChoice == "tictactoe":
                    tictactoe.tictactoeGameLoop()
                    break
        elif userChoice == "settings":
            while True:
                gameChoice = input("What game settings would you like to change (hangman, connectfour, tictactoe)")
                if gameChoice == "hangman":
                    hangman.wordListChanging()
                if gameChoice == "connectfour":
                    connectfour.connectfourSettingsLoop()
                if gameChoice == "tictactoe":
                    tictactoe.tictactoeSettingsLoop()
                    break
        elif userChoice == "quit":
            quit()
        else:
            print("Invalid input")