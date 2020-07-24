

print("Welcome to trivia! \nAll you have to answer the questions that I ask you \nLet's see how much you know about the NBA")
def main():
	gameover = False
	while not gameover:
		ask = input("\nDo you think your ready?: ")
		if ask != "yes":
			print("\nI guess you're not up for the challenge :(\nCome back when you're ready!")
			return 0
		else:
			print("LETS GET STARTED!")

		correctanswers = 0

		#1)
		question1 = input("\nQuestion #1\nWho has the most missed shots in the NBA? \na)LeBron James \nb)Kobe Bryant \nc)Steph Curry \n:").lower()
		if question1 != "b":
			print("Wrong answer :(")
			correctanswers +=0

		else:
			print("Good job!")
			correctanswers +=1

		#2)
		question2 = input("\nQuestion #2 \nWhat NBA team has won the most chapionships?: ").lower()
		if question2 != "celtics" and question2 != "boston" and question2 != "boston celtics":
			print("Wrong answer :( ")
			correctanswers +=0

		else:
			print("Good job! ")
			correctanswers +=1

		#3)
		question3 = input("\nQuestion #3 \nHow many teams are in the NBA?: ").lower()
		if question3 != "30" and question3 != "30 teams":
			print("Wrong answer :( ")
			correctanswers +=0

		else:
			print("Good job! ")
			correctanswers +=1

		#4)
		question4 = input("\nQuestion #4 \nWho had the longest NBA career?: ").lower()
		if question4 != "vince carter":
			print("Wrong answer :( ")
			correctanswers +=0

		else:
			print("Good job! ")
			correctanswers +=1

		#5
		question5 = input("\nQuestion #5 \nWhat team won the 2019 NBA championship?: ").lower()
		if question5 != "raptors" and question5 != "toronto" and question5 != "toronto raptors":
			print("Wrong answer :( ")
			correctanswers +=0
		
		else:
			print("Good job!")
			correctanswers +=1

		#6
		question6 = input("\nQuestion #6 \nWho has the record for the most 3's in a game? \na)Klay Thompson \nb)Steph Curry \nc)James Harde \n: ").lower()
		if question6 != "a":
			print("Wrong answer :( ")
			correctanswers +=0
		else:
			print("Good job!")
			correctanswers +=1


		#7
		question7 = input("\nQuestion #7 \nWho owns the Dallas Mavericks?: ").lower()
		if question7 != "mark cuban":
			print("Wrong answer :( ")
			correctanswers +=0
		else:
			print("Good job!")
			correctanswers +=1
		
		#8
		question8 = input("\nQuestion #8 \nHow many NBA chapionships have the LA Lakers won?: ")
		if question8 != "16":
			print("Wrong answer :( ")
			correctanswers +=0
		else:
			print("Good job!")
			correctanswers +=1

		#9
		question9 = input("\nQuestion #9 \nWhich NBA player only made one 3 point shot?: ").lower()
		if question9 != "shaq" and question9 != "shaquille o'neal":
			print("Wrong answer :( ")
			correctanswers +=0
		else:
			print("Good job!")
			correctanswers +=1

		
		if correctanswers < 4:
			print("\nYou might want to study harder ")
		elif 3 < correctanswers < 7:
			print("\nYou can do better ")
		else:
			print("\nGreat job! ")


		print(f"You got {correctanswers} out of 8 questions correct")

		choice = input("\nDo you want to play again (yes or no)?: ")
		if choice != "yes" and choice != "y":
			print("Okay, bye :( ")
			gameover = True
	return 0 
main()


