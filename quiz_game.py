print("hi!! WEOLCOME to QUIZ GAME")

play = input("Woud you like to play this game? ")
if play.upper() !="YES":
    print("BB Have Fun")
    quit()

print("okaayy!! Lets  Play (-_-)")
score = 0
questions = 0

ans1 = input("What does CPU stand for?")
questions += 1
if ans1.lower() == "central processing unit":
    print("U r Correct :)")
    score += 1

else: print("U r Incorrect..")

ans2 = input("What does GPU stand for?").lower()
questions += 1
if ans2== "graphics processing unit":
    print("U r Correct :)")
    score += 1
    

else: print("U r Incorrect..")

ans3 = input("What does RAM stand for?")
questions += 1
if ans3.lower() == "random access memory":
    print("U r Correct :)")
    score += 1

else: print("U r Incorrect..")

ans4 = input("What does ROM stand for?")
questions += 1
if ans4.lower() == "read only memory":
    print("U r Correct :)")
    score += 1

else: print("U r Incorrect..")

print("You got " + str(score) + " out of " + str(questions))
print ("marks = " +str((score/questions)*100)+"%")