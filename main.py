

print(
  "welcome to the trivia game \nI ask you questions and you see if you can answer them"
)
ask = input("do you think your ready?")
if ask != "yes":
  gameover = True
  print("I guess your not up for the challenge")
else:
  print("LETS GET STARTED!")

correctanswers = 0
player = -1

#1)
question1 = input("\nwhat is the capitol of massachusetts?: ")
if question1 != "boston":
	gameover = True
	print("wrong answer :(")
	correctanswers +=0

else:
	print("good job!")
	correctanswers +=1

#2)
question2 = input("\nWhat NBA team has won the most chapionships?: ")
if question2 != "celtics" :
	gameover = True
	print("wrong answer :( ")
	correctanswers +=0

else:
	print("good job! ")
	correctanswers +=1

#3)
question3 = input("\nhow many teams are in the NBA?: ")
if question3 != "30":
	gameover = True
	print("wrong answer :( ")
	correctanswers +=0

else:
	print("good job! ")
	correctanswers +=1

#4)
question4 = input("\nwho had the longest NBA career?: ")
if question4 != "vince carter":
	gameover = True
	print("wrong answer :( ")
	correctanswers +=0

else:
	print("good job! ")
	correctanswers +=1

	print(f"\nyou got {correctanswers}/4 right")