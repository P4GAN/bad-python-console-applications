width = 3
height = 3

winWidth = 3
winHeight = 3

def tictactoeSettingsLoop():
    global width 
    global height 
    global winWidth
    global winHeight
    while True:
        print("Please input, separated by a comma and no spaces: width, height, winwidth and winheight (how many pieces in a row up or down required to win)")
        print("Note: winheight and winwidth must be the same, greater than zero, and smaller than height and width")
        settings = input("Please input: ").split(",")
        if len(settings) == 4:
            width, height, winWidth, winHeight = settings
            if width.isdigit() and height.isdigit() and winWidth.isdigit() and winHeight.isdigit(): 
                width = int(width)
                height = int(height)
                winWidth = int(winWidth)
                winHeight = int(winHeight)
                if winWidth == winHeight and 0 < winWidth <= width and 0 < winHeight <= height and width > 0 and height > 0:
                    break
        print("Incorrect settings, try again")
        width = 3
        height = 3
        winWidth = 3
        winHeight = 3


def tictactoeGameLoop():
    import random 

    grid = []


    for y in range(height):
        row = []
        for x in range(width):
            row.append(" ")
        grid.append(row)

    def checkWin(winCharacter):
        for y in range(winHeight):
            row = "".join(grid[y])
            if (winWidth * winCharacter) in row:
                return True
        for x in range(winWidth):
            column = "".join([row[x] for row in grid])
            if (winHeight * winCharacter) in column:
                return True
        for y in range(0, 1 + width - winWidth):
            for x in range(1 + height - winHeight):
                if grid[y][x] == winCharacter and grid[y + 1][x + 1] == winCharacter and grid[y + 2][x + 2] == winCharacter:
                    return True
        for y in range(0, 1 + width - winWidth):
            for x in range(winHeight - 1, height):
                if grid[y][x] == winCharacter and grid[y + 1][x - 1] == winCharacter and grid[y + 2][x - 2] == winCharacter:
                    return True
        return False

    def drawGrid():
        for i in range(height - 1):
            print("|".join(grid[i]))
            print("-" * (width * 2 - 1))
        print("|".join(grid[-1]))
        print("")


    def move(character, computer = False):
        while True:
            if computer:
                move = [random.randint(0, width - 1), random.randint(0, width - 1)]
                print("Computer played " + str(move[0]) + "," + str(move[1]))
                if grid[int(move[1])][int(move[0])] == " ":
                    break
            else:
                move = input("Move (input a row and column separated by a comma, where the first row and column is 0): ").split(",")
                try:
                    grid[int(move[1])][int(move[0])]
                except:
                    print("Invalid move")
                else:
                    if grid[int(move[1])][int(move[0])] != " ":
                        print("Invalid move, the square is occupied")
                    else:
                        break
        grid[int(move[1])][int(move[0])] = character

    while True:
        computerQuestion = input("Would you like to vs the computer? (y/n)")
        if computerQuestion == "y":
            computerGamemode = True
            break
        elif computerQuestion == "n":
            computerGamemode = False
            break
        else:
            print("Please answer y or n")

    player1Computer = False
    player2Computer = False

    if computerGamemode:
        if random.randint(0, 1) == 1:
            player1Computer = True
            print("Computer goes first")
        else:
            player2Computer = True
            print("Player goes first")

    while True:
        move("#", player1Computer)
        drawGrid()
        if checkWin("#"):
            print('# wins')
            break
        move("O", player2Computer)
        drawGrid()
        if checkWin("O"):
            print('O wins')
            break


if __name__ == "__main__":
    print("This is the wrong file, please run 'mainGame.py'")