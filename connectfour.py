width = 7
height = 6

winWidth = 4
winHeight = 4

def connectfourSettingsLoop():
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
        width = 7
        height = 6
        winWidth = 4
        winHeight = 4


def connectfourGameLoop():
    import random 


    grid = []

    for y in range(height):
        row = []
        for x in range(width):
            row.append(" ")
        grid.append(row)

    def checkWin(winCharacter):
        for y in range(height):
            row = "".join(grid[y])
            if (winWidth * winCharacter) in row:
                return True
        for x in range(width):
            column = "".join([row[x] for row in grid])
            if (winHeight * winCharacter) in column:
                return True
        for y in range(0, 1 + height - winHeight):
            for x in range(0, 1 + width - winWidth):
                win = True
                for i in range(winHeight):
                    if grid[y + i][x + i] != winCharacter:
                        win = False
                if win == True:
                    return True

        for y in range(0, 1 + height - winHeight):
            for x in range(winWidth - 1, width):
                win = True
                for i in range(winHeight):
                    if grid[y + i][x - i] != winCharacter:
                        win = False
                if win == True:
                    return True

    def drawGrid():
        for i in range(height - 1):
            print("|".join(grid[i]))
            print("-" * (width * 2 - 1))
        print("|".join(grid[-1]))
        print("")


    def findPositionByColumn(column):
        for i in reversed(range(height)):
            if grid[i][column] == " ":
                return [column, i]
        return False

    def move(character, computer = False):
        while True:
            if computer:
                movePosition = findPositionByColumn(random.randint(0, width - 1))
                if movePosition:
                    print("Computer played row " + str(movePosition[1]))
                    break
            else:
                move = input("Move (input a row, starting from 0): ")
                try:
                    movePosition = findPositionByColumn(int(move))
                except:
                    print("Not a valid move")
                else:
                    if not movePosition:
                        print("Not a valid move, the column is full")
                    else:
                        break
        grid[movePosition[1]][movePosition[0]] = character

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
    