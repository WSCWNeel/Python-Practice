play = "yes"
score = 0
print("Hello")
#Question of User's Name and the code remembering the answer
name= input("What is your name?")
#Greeting the User and introducing the quiz
print("Welcome to the Quiz", name)
print("This quiz is about guessing your favourite color according to me")
#Asking the user a question
answer=input("What is your favourite color?")
#Telling the user the correct answer
if answer == " Blue":
    print("Correct!") 
elif answer == "":
    print("Not Sure?")
    print("It's Blue")
else:
    print("Wrong answer")
    print("The correct answer was the color Blue")

question_prompts = [
    "How hungry are you?/n(a) Very Hungry/n(b) Maybe Hungry/n(c) Not Hungry"
]

if answer == " Blue":
    score =+ 100
player_input = input("Do you want to try again?")

if player_input == "yes":

break

#Ending the Quiz
print("Your final score is", score)
print("Thank you for doing this quiz and goodbye")