score = 0
print ("Hello")
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

if answer == " Blue":
    score =+ 100
#Ending the Quiz
print("Your final score is", score)
print("Thank you for doing this quiz and goodbye")