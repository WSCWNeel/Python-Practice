score = 0
play ="yes"

#ask the user their name
name = input("What's your name?")

#Greetings to the user and close the quiz
print("Welcome to the quiz")
print("This quiz is about capital cities of the world")

#Check number of question attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-4")
        tries = int(tries)
        break
    except:
        print("That's not a number")

#Start the quiz
while play == "yes":

    #Ask the user a question
    question = "What is the capital of New Zealand?"
    a = "Wellington"
    b = "Auckland"
    c = "London"
    d = "Christchurch"
    answer = input("{}/nA., {}/nB., {}/nC., {}/nD.". format(question, a, b, c, d)).lower()

#Check the user's answer
if answer == a or answer == "Wellington":
    print("Correct")
    score =+ 100
    break
elif answer == "":
    print("Not sure?")
else:
    print("Wrong")

    question_attempts =- 1
print("The answer is Wellington.")

#End the quiz
print("Well done {}. You finished the quiz. Your final score was {}".format(name, score))

#Replay
play = input("Do you want to play again?").lower()