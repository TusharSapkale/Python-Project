print ("Welcome to my game quiz game..!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print ("Okay! Lets go :) ")

score = 0

answer = input("Who is the prime minister of India? ").lower()
if answer == "narendra modi":
    print ("Correct!")
    score += 1
else: print("Incorrect!")

answer = input("What is the capital of India? ").lower()
if answer == "delhi":
    print ("Correct!")
    score += 1
else: print("Incorrect!")

answer = input("What is the most popular and most watched sport in India?  ").lower()
if answer == "cricket":
    print ("Correct!")
    score += 1
else: print("Incorrect!")

answer = input("How many teams are playing in IPL 2024 tournament?  ").lower()
if answer == "10":
    print ("Correct!")
    score += 1
else: print("Incorrect!")

answer = input("Which team will win IPL 2024?  ").lower()
if answer == "rcb":
    print ("Correct!")
    score += 1
else: print("Incorrect!")

print ("Your have Scored is ", (score/5)*100 , "in the contest...!" )


