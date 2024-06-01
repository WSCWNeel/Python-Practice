guesses = []
LARGEST_ANIMALS_ANSWERS = ["african elephant", "komodo dragon", "hippopotamus", "bison", "blue whale", "indian rhinoceros", "saltwater crocodile", "elephant seals", "polar bear", "giant squid"]

#Welcome to the quiz
def intro():
    #Greeting the user and getting them to start the quiz
    name = input("What is your name?")

    print("Welcome to the quiz", name)
    print("This quiz is about guessing the top 10 most largest animals(once you're done with the game type a wrong answer)")

def getLives():
        while True:
            lives = input("How many tries/chances/lives do you want for this quiz?")
            try:
                 lives = int(lives)
                 if lives >= 0:
                      return lives
                 else:
                      print("Just choose a proper number")
            except:
                print("That ain't a number buddy, try again")


def inList(answers, list):
    if answers in list:
         return True
    else:
         return False

def isCorrect(answer, LARGEST_ANIMALS):
     if answer in LARGEST_ANIMALS:
          return True
     else:
          return False

#the main code
intro()
lives = getLives()
score = 0
while lives > 0:
    answer = input("What is the top 10 largest animals in the world?").lower()

    if inList(answer, LARGEST_ANIMALS_ANSWERS):
         if inList(answer, guesses):
            print("You've guessed that")
         else:
              print("Correct")
              score += 5
              guesses.append(answer)
              print("You have guessed {}, Your score is {}, You have {} chances left".format(len(guesses),(score), (lives)))
    else:
         print("Wrong")
         lives -= 1
         print("You have guessed {}, Your score is {}, You have {} chances left".format(len(guesses),(score), (lives)))

print("Game over, your final score is {}".format(score))
