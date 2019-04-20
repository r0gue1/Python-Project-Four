from random import randint

def main() :
    # Variables
    ballCount = 0
    playerBall = 0
    playerTurn = 0
    computerMode = 0

   # Process
    playerTurn = randint(0, 1)
    ballCount = randint(10, 100)
    computerMode = randint(0, 1)
# r0gue1 # added instructions to end user and rules of Nym's Game
#        # made formatting edits to string outputs
    print("The initial pot contains", ballCount,"balls.\
          \nNym's Game conditions:\
          \nEach player takes a turn drawing up to half of the balls.\
          \nThe last player to draw a ball loses the game of Nym.")

    while ballCount > 1:
        if playerTurn == 0:
            if computerMode == 1:
                print("Computer mode: Dumb")
                ballTaken = computerDumbMode(ballCount)
                print("Computer takes ... ", ballTaken)
                ballCount = ballCount - ballTaken
                print("The new ball count is... ", ballCount)
                playerTurn = 1
            else:
                print("Computer mode: Smart")
                ballTaken = computerSmartMode(ballCount)
                print("Computer takes... ", ballTaken)
                ballCount = ballCount - ballTaken
                print("The new ball count is... ", ballCount)
                playerTurn = 1
        else:
            print("Human player's turn:")
            ballCount = ballCount - userTurn(ballCount)
            print("The new ball count is... ", ballCount)
            playerTurn = 0

    #output
    if playerTurn == 1:
        print("Computer wins!")
    else:
        print("You win!")


def userTurn(ballCount):
    playerBall = int(input("How many balls do you want to take?  "))

    if playerBall == 0:
        while playerBall == 0:
            print("You need to take at least 1 ball")
            playerBall = int(input("How many balls do you want to take?  "))

    if playerBall <= ballCount:
        while playerBall > ballCount / 2:
            print("You cannot take more than half the total amount of balls... ")
            playerBall = int(input("How many balls do you want to take?  "))

    if playerBall > ballCount:
        while playerBall > ballCount / 2:
            print("You cannot take more balls than what is available")
            playerBall = int(input("How many balls do you want to take?  "))

    return playerBall


def computerDumbMode(ballCount):
    if ballCount % 2 == 0:
        value = randint(1, ballCount / 2)
    else:
        value = randint(1, (ballCount - 1) / 2)
    return value

def computerSmartMode(ballCount):
    if ballCount > 63:
        value = ballCount - 63
    if 31 < ballCount <= 63:
        value = ballCount - 31
    if 15 < ballCount <= 31:
        value = ballCount - 15
    if 7 < ballCount <= 15:
        value = ballCount - 7
    if 3 < ballCount <= 7:
        value = ballCount - 3
    if 1 < ballCount <= 3:
        value = 1

    return value


main()
