#Number Guessing Game
import random

def getRandomNumber():
    return random.randint(1, 100)

def getUserGuess(counter):
    count = counter
    userGuess = -1
    while userGuess != 0:
        try:
            if count == 0:
                userGuess = int(input("Enter your guess (between 1 and 100) Note: 0 is for Exit: "))
            else:
                userGuess = int(input("Enter your next guess: "))
            if userGuess == 0:
                print("Thanks for playing! Goodbye.")
                return {"userGuess": userGuess, "counter": count}
            if 1 <= userGuess <= 100:
                count += 1
                return {"userGuess": userGuess, "counter": count}
            else:
                print("Please enter a number between 1 and 100.Note: 0 is for Exit:")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def getResults(counter):
    print("Congratulations! You guessed the number.")
    print(f"It took you {counter} tries to guess the number.")

def guessNumber(randomNumber):
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    print("Enter 0 to quit the game.")
    data = getUserGuess(0)

    while data.get("userGuess") != 0:
            if (data.get("userGuess") - randomNumber) <= 10 and (data.get("userGuess") - randomNumber) > 0:
                print("You're getting close! Go some lower.")
            elif (data.get("userGuess") - randomNumber) >= -10 and (data.get("userGuess") - randomNumber) < 0:
                print("You're getting close! Go some higher.")
            elif (data.get("userGuess") - randomNumber) < -10:
                print("Too Low! Try again.")
            elif data.get("userGuess") > randomNumber:
                print("Too High! Try again.")
            else:
                getResults(data.get("counter"))
                break
            data= getUserGuess(data.get("counter"))
def main():
    randomNumber = getRandomNumber()
    guessNumber(randomNumber)

main()