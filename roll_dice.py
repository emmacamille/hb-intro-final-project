# roll the dice game

import random

#list_of_outcomes = ["sushi", "burrito", "cheesesteak", "pizza", "ramen", "deli sandwich"]

def roll_the_dice(outcomes):

	print "So, you're hungry and indecisive. I see... Well, would you like to roll a dice for munching ideas?" 
	yes_no_answer = raw_input("Yes or no?")

	if yes_no_answer == "NO" or yes_no_answer == "no":
		print "Seriously, you're that indecisive. Fine."
			#end program
	else: 
		print random.choice(list_of_outcomes)

#print roll_the_dice(list_of_outcomes)

# custom dice 


def custom_dice():
	
	dice_outcomes = []	

	print "It's nice to be able to pick the options on the dice. You are going to be able to add up to six food items to your dice."

	while len(dice_outcomes) < 6: # six options

		new_outcomes = raw_input("What is item you would like to add to the list?") 

	 	if (new_outcomes in dice_outcomes):
	 		# if food item exists in list, do not add
	 		print "You've already added that item to the dice!"
	 	else: 
	 		# if food item does not exist, add to list
	 		dice_outcomes.append(new_outcomes)

	final_choice = random.choice(dice_outcomes)

	print "And the dice says... %s" %(final_choice)

print custom_dice()
			