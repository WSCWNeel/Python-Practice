playGame = "True"
print("Hello")
#Question of User's Name and the code remembering the answer
name= input("What is your name?")
#Greeting the User and introducing the quiz
print("Welcome to the Quiz", name)
print("This quiz is about guessing questions answers according to me")
print("Hope you get none of it wrong, > _ o")
#No. of tries


#Starting the quiz?
while playGame == "yes":
    score = 0
#`Working code
print("The options are: Red, Blue, White and Black (and if you want press enter and don't answer)")
answer=input("What is your favourite color?")
#Telling the user the correct answer
if answer == " Blue":
    print("Correct!")
elif answer == "blue":
    print("Correct")
elif answer == "Blue":
    print("Correct")
elif answer == " blue":
    print("Correct")
elif answer == "":
    print("Not Sure?")
    print("It's Blue")
else:
    print("Wrong answer")
    print("The correct answer was the color Blue")

if answer == " Blue":
    score =+ 100
elif answer == "Blue":
    score =+ 100
elif answer == "blue":
    score =+ 100
elif answer == " blue":
    score =+ 100
else:
    score =+ 0

print("The options are: Yes, No, (press enter for the answer) and Maybe")
answer=input("Are you hungry?")
#Telling the user the correct answer
if answer == " Maybe":
    print("Correct!")
elif answer == "maybe":
    print("Correct")
elif answer == "Maybe":
    print("Correct")
elif answer == " maybe":
    print("Correct")
elif answer == "":
    print("Not Sure?")
    print("It's Maybe")
else:
    print("Wrong answer")
    print("The correct answer was Maybe")

if answer == " Maybe":
    score =+ 200
elif answer == "Maybe":
    score =+ 200
elif answer == "maybe":
    score =+ 200
elif answer == " maybe":
    score =+ 200
else:
    score =+ 0

#Code for ending the quiz as well...
if playGame == input("Do you want to try again?"):

#Ending the Quiz

 if playGame == True:
    print("Restart the quiz to do the quiz again.")   
else:
    print("Your final score is", score)
    print("Thank you for doing this quiz and goodbye")

play = "yes"