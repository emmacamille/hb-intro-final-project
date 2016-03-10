import random

class DiceEdit(object):
	def __init__(self, dice_category):
		self.dice_category = dice_category.lower()
		self.dice_outcomes = []

	def add_to_dice(self, food_list):
		# self.dice_outcomes.extend(food)
		for item in food_list:
			# item_upper = self.dice_outcomes.upper()
			if item not in self.dice_outcomes:
				self.dice_outcomes.append(item)
		# food you pass in much be a list b/c extend
		# what if food item already exists
		# deal with case sensitivity

	def remove_from_dice(self, food):
		self.dice_outcomes.remove(food)
		# deal with case sensitivity

	def random_outcome(self):
		print "Are you ready to roll the dice?"
		yes_no_answer = raw_input("Yes or no?")

		if yes_no_answer == "NO" or yes_no_answer == "no" or yes_no_answer == "No":
			print "Seriously, you're that indecisive. Fine."
			#end program
		else: 
			return random.choice(self.dice_outcomes)

	# def return_outcomes(self):
	# 	# print/return dice.outcomes

	# def save_custom_to_file(self):

	# def read_custom_file(self):

