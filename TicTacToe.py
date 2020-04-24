import sys

field = ["",
         "=", "=", "=",
         "=", "=", "=",
         "=", "=", "="]

fieldNumbers = ["",
                "1", "2", "3",
                "4", "5", "6",
                "7", "8", "9"]


# functions to check the different rows for a win
def checkTopRow():
    if (field[1] == "X" and field[2] == "X" and field[3] == "X") or (
            field[1] == "O" and field[2] == "O" and field[3] == "O"):
        if field[1] == "X":
            return "X"
        return "O"
    return False


def checkMidRow():
    if (field[4] == "X" and field[5] == "X" and field[6] == "X") or (
            field[4] == "O" and field[5] == "O" and field[6] == "O"):
        if field[4] == "X":
            return "X"
        return "O"
    return False


def checkBottomRow():
    if (field[7] == "X" and field[8] == "X" and field[9] == "X") or (
            field[7] == "O" and field[8] == "O" and field[9] == "O"):
        if field[7] == "X":
            return "X"
        return "O"
    return False


def checkLeftColumn():
    if (field[1] == "X" and field[4] == "X" and field[7] == "X") or (
            field[1] == "O" and field[4] == "O" and field[7] == "O"):
        if field[1] == "X":
            return "X"
        return "O"
    return False


def checkMidColumn():
    if (field[2] == "X" and field[5] == "X" and field[8] == "X") or (
            field[2] == "O" and field[5] == "O" and field[8] == "O"):
        if field[2] == "X":
            return "X"
        return "O"
    return False


def checkRightColumn():
    if (field[3] == "X" and field[6] == "X" and field[9] == "X") or (
            field[3] == "O" and field[6] == "O" and field[9] == "O"):
        if field[3] == "X":
            return "X"
        return "O"
    return False


def checkDiag1():
    if (field[1] == "X" and field[5] == "X" and field[9] == "X") or (
            field[1] == "O" and field[5] == "O" and field[9] == "O"):
        if field[1] == "X":
            return "X"
        return "O"
    return False


def checkDiag2():
    if (field[3] == "X" and field[5] == "X" and field[7] == "X") or (
            field[3] == "O" and field[5] == "O" and field[7] == "O"):
        if field[3] == "X":
            return "X"
        return "O"
    return False


# checking for win with all functions from above combined.
def checkWin():
    if checkTopRow() == "X":
        return "X"
    if checkTopRow() == "O":
        return "O"
    if checkMidRow() == "X":
        return "X"
    if checkMidRow() == "O":
        return "O"
    if checkBottomRow() == "X":
        return "X"
    if checkBottomRow() == "O":
        return "O"
    if checkLeftColumn() == "X":
        return "X"
    if checkLeftColumn() == "O":
        return "O"
    if checkMidColumn() == "X":
        return "X"
    if checkMidColumn() == "O":
        return "O"
    if checkRightColumn() == "X":
        return "X"
    if checkRightColumn() == "O":
        return "O"
    if checkDiag1() == "X":
        return "X"
    if checkDiag1() == "O":
        return "O"
    if checkDiag2() == "X":
        return "X"
    if checkDiag2() == "O":
        return "O"
    return False


# getting pick
def getPick():
    pick = input("Please pick a spot to place your symbol. (1-9)")
    return pick


# executing player 1's move
def Player1Act():
    pick = getPick()
    if pick != "1" and pick != "2" and pick != "3" and pick != "4" and pick != "5" and pick != "6" and pick != "7" and pick != "8" and pick != "9":
        print("Invalid input!")
        Player1Act()
    else:
        if field[int(pick)] != "X" and field[int(pick)] != "O":
            field[int(pick)] = "X"
        else:
            print("Field already occupied!")
            Player1Act()


# executing player 2's move
def Player2Act():
    pick = getPick()
    if pick != "1" and pick != "2" and pick != "3" and pick != "4" and pick != "5" and pick != "6" and pick != "7" and pick != "8" and pick != "9":
        print("Invalid input!")
        Player2Act()
    else:
        if field[int(pick)] != "X" and field[int(pick)] != "O":
            field[int(pick)] = "O"
        else:
            print("Field already occupied!")
            Player2Act()


# checking if there is a draw
def checkDraw():
    if (field[1] == "X" or field[1] == "O") and \
            (field[2] == "X" or field[2] == "O") and \
            (field[3] == "X" or field[3] == "O") and \
            (field[4] == "X" or field[4] == "O") and \
            (field[5] == "X" or field[5] == "O") and \
            (field[6] == "X" or field[6] == "O") and \
            (field[7] == "X" or field[7] == "O") and \
            (field[8] == "X" or field[8] == "O") and \
            (field[9] == "X" or field[9] == "O"):
        return True
    else:
        return False


# printing the field
def printField():
    print(field[1] + " " + field[2] + " " + field[3])
    print(field[4] + " " + field[5] + " " + field[6])
    print(field[7] + " " + field[8] + " " + field[9])


# printing the field's numbers'
def printFieldNumbers():
    print(fieldNumbers[1] + " " + fieldNumbers[2] + " " + fieldNumbers[3])
    print(fieldNumbers[4] + " " + fieldNumbers[5] + " " + fieldNumbers[6])
    print(fieldNumbers[7] + " " + fieldNumbers[8] + " " + fieldNumbers[9])


# game starting stuff
print("Welcome to Tic-Tac-Toe!")
print("-----------------------")
print(
    field[1] + " " + field[2] + " " + field[3] + "  " + fieldNumbers[1] + " " + fieldNumbers[2] + " " + fieldNumbers[3])
print(
    field[4] + " " + field[5] + " " + field[6] + "  " + fieldNumbers[4] + " " + fieldNumbers[5] + " " + fieldNumbers[6])
print(
    field[7] + " " + field[8] + " " + field[9] + "  " + fieldNumbers[7] + " " + fieldNumbers[8] + " " + fieldNumbers[9])
gameActive = True
# managing turns and wins/draws
while gameActive:
    print("It's player 1's turn")
    Player1Act()
    printField()
    win = checkWin()
    if win:
        print("Player 1 wins!!")
        sys.exit()
        gameActive = False
    draw = checkDraw()
    if draw:
        print("Draw!")
        sys.exit()

    print("It's player 2's turn")
    Player2Act()
    printField()
    win = checkWin()
    if win:
        print("Player 2 wins!")
        sys.exit()
        gameActive = False
