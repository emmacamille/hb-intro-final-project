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
	outcomes_made = 1

	while outcomes_made < 7:

		print "It's nice to be able to pick the options on the dice. You are going to be able to add up to six food items to your dice."
		new_outcomes = raw_input("What is the number %i item you would like to add to the list?") %(outcomes_made)

	 	if (outcome in dice_outcomes):
	 		print "You've already added that item to the dice!"
	 	else: 
	 		outcomes_made = outcomes_made + 1
	 		dice_outcomes.append(new_outcomes)

	return random.choice(dice_outcomes)

print custom_dice()
			