import random
from diceRemarks import *

class DiceEdit(object):
	def __init__(self, dice_category):
		self.dice_category = dice_category.lower()
		self.dice_outcomes = []

	def add_to_dice(self, food_list):
		for item in food_list:
			if item not in self.dice_outcomes:
				self.dice_outcomes.append(item)
			else:
				print "That item is already on the dice."
		# food you pass in much be a list b/c extend
		# what if food item already exists
		# deal with case sensitivity

	def custom_dice(self):
		# using dice_outcomes: 
		# while loop: while answer is not "0", add food item to list
		# if new_item = "0": exit, dice complete.
		# else: self.dice_outcomes.append(new_item)
		print "You'd like to create your own dice? Cool! Here are the rules:" + "\n" + "1. Enter as many food items as you'd like." + "\n" + "2. Once you have added everything, type 0 (the number zero)." + "\n" + "3. Get unhungry!"

		while len(self.dice_outcomes) < 6: # six options

			new_item = raw_input("What is item you would like to add to the list?") 
			if new_item == "0":
				if len(self.dice_outcomes) == 0:
					print "That's not how it works here. You must have at least 1 item on the dice."
				else:
					break
		 	elif (new_item in self.dice_outcomes):
		 		# if food item exists in list, do not add
		 		print "You've already added that item to the dice!"
		 	else: 
		 		# if food item does not exist, add to list
		 		self.dice_outcomes.append(new_item)

	def remove_from_dice(self, food):
		self.dice_outcomes.remove(food)
		# deal with case sensitivity

	def yes_no_answer(self):
		print "Are you ready to roll the dice?"
		yes_no_answer = raw_input("Yes or no?")

		if yes_no_answer in ("n", "N", "NO", "no", "No"):
			print "\n \n" + random.choice(no_answer) + "\n \n"
			#end program
		else: 
			return True

	def random_outcome(self, yes_no):
			return random.choice(self.dice_outcomes)


	# def return_outcomes(self):
	# 	# print/return dice.outcomes

	# def save_custom_to_file(self):

	# def read_custom_file(self):

	# def view_menu(self):
		# elif yes_no_answer in ("menu", "MENU", "Menu"):
		# 	print self.dice_outcomes