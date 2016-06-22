import random
import time
running = True
AI1choice = 0
AI2choice = 0

print("Just so everything is clear, the 'win' 'loss' thing is by AI1's point of view.")
time.sleep(2)

def judge(choice1, choice2):
    global answer
    if choice1 == choice2:
        answer = "draw"
    #Not shure if this will work.
    elif choice2 == choice1:
        answer = "draw"
    elif choice1 == "rock":
        if choice2 == "paper":
            answer = "loss"
        elif choice2 == "scissors":
            answer = "win"
        else:
            answer = "error"
    elif choice1 == "paper":
        if choice2 == "rock":
            answer = "win"
        elif choice2 == "scissors":
            answer = "loss"
        else:
            answer = "error"
    elif choice1 == "scissors":
        if choice2 == "rock":
            answer = "loss"
        elif choice2 == "paper":
            answer = "win"
        else:
            answer = "error"
    else:
        answer = "error"
    return answer

def formatChoice(choice, real):
    global feedback
    if choice == 1:
        feedback = "rock"
    elif choice == 2:
        feedback = "paper"
    elif choice == 3:
        feedback = "scissors"
    elif choice > 3:
        choice = real
    else:
        feedback = "error"
    return feedback

while running == True:
    AI1choice = formatChoice(random.randint(1, 3), AI1choice)
    fakeAI1choice = formatChoice(random.randint(1, 4), AI1choice)
    AI2choice = formatChoice(random.randint(1, 3), AI2choice)
    fakeAI2choice = formatChoice(random.randint(1, 4), AI2choice)
    print("AI1 is thinking " + fakeAI1choice)
    print("AI2 is thinking " + fakeAI2choice)
    print("Do you think AI1 is making the right choice?")
    Pinput = input(": ")
    if Pinput == "yes":
        print("Ok, this is AI1's real choice, " + AI1choice)
        print("and this is AI2's real choice, " + AI2choice)
        result = judge(AI1choice, AI2choice)
        print(result)
    elif Pinput == "no":
        Pinput = input("What do you think AI1 should pick? : ")
        if Pinput == "rock":
            random.randint(1, 3)
            if
        
           
