class DiceEdit(object):
	def __init__(self, dice_category):
		self.dice_category = dice_category.lower()
		self.dice_outcomes = []

	def add_to_dice(self, food_list):
		# self.dice_outcomes.extend(food)
		for item in food_list:
			item_upper = self.dice_outcomes.upper()
			if item_upper not in food_list:
				self.dice_outcomes.append(item_upper)
		# food you pass in much be a list b/c extend
		# what if food item already exists
		# deal with case sensitivity

	def remove_from_dice(self, food):
		self.dice_outcomes.remove(food)
		# deal with case sensitivity

	def random_outcome(self):
		# random.choice from dice_outcomes

	def return_outcomes(self):
		# print/return dice.outcomes

