

print("Welcome to trivia! \nAll you have to answer the questions I ask you \nlet's see how much you know about the NBA")
def main():
	ask = input("\ndo you think your ready?: ")
	if ask != "yes":
		print("\nI guess your not up for the challenge :(\ncome back when your ready!")
		return 0
	else:
		print("LETS GET STARTED!")

	correctanswers = 0

	#1)
	question1 = input("\nWho has the most missed shots in the NBA? \na)LeBron James \nb)Kobe Bryant \nc)Steph Curry \n:")
	if question1 != "b" and question1 != "B":
		print("wrong answer :(")
		correctanswers +=0

	else:
		print("good job!")
		correctanswers +=1

	#2)
	question2 = input("\nWhat NBA team has won the most chapionships?: ")
	if question2 != "celtics" and question2 != "boston" and question2 != "boston celtics":
		print("wrong answer :( ")
		correctanswers +=0

	else:
		print("good job! ")
		correctanswers +=1

	#3)
	question3 = input("\nhow many teams are in the NBA?: ")
	if question3 != "30" and question3 != "30 teams":
		print("wrong answer :( ")
		correctanswers +=0

	else:
		print("good job! ")
		correctanswers +=1

	#4)
	question4 = input("\nwho had the longest NBA career?: ")
	if question4 != "vince carter":
		print("wrong answer :( ")
		correctanswers +=0

	else:
		print("good job! ")
		correctanswers +=1

	#5
	question5 = input("\nWhat tem won the 2019 NBA championship?: ")
	if question5 != "raptors" and question5 != "toronto" and question5 != "toronto raptors":
		print("wrong answer :( ")
		correctanswers +=0
	
	else:
		print("good job!")
		correctanswers +=1

	#6
	question6 = input("\nWho has the record for the most 3's in a game? \na)Klay Thompson \nb)Steph Curry \nc)Kevin Durant \n:")
	if question6 != "a" and question6 != "A":
		print("wrong answer :( ")
		correctanswers +=0
	else:
		print("good job!")
		correctanswers +=1

	print(f"\nyou got {correctanswers}/6 right")
main()