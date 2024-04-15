import random

#Function to generate numbers (3.1)
def numGen():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b

#Function to get players answer (3.2)
def playerInput(a, b):
    while True:
        try:
            userAnswer = int(input("What is {} x {}? ".format(a, b)))
            return userAnswer
        except ValueError:
            print("Please enter a valid integer.")
            
#Checks to see if player answer same as actual answer (3.3)
def checkAnswer(a, b, userAnswer):
    c = a * b
    return c == userAnswer

#Starts the game (3.4)
def startGame():
    score = 0
    print("Let's play a multiplication game!\n")
    while True:
        a, b = numGen()
        print("What is product of {} and {}? ".format(a, b))
        c = playerInput(a, b)
        if checkAnswer(a, b, c):
            score += 1
            print("Correct! Your score is {}".format(score))
            while True:
                continuePlaying = input("Do you want to play again? (y/n) ")
                if continuePlaying.lower() == "n":
                    return
                elif continuePlaying.lower() == "y":
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Incorrect. You lost")
            return

#Starts Game (3.5)
startGame()