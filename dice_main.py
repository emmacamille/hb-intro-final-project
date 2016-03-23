from DiceMainClass import *
from mystery_box import *
from diceRemarks import *

sober_dice_edit = DiceEdit("sober")
drunk_dice_edit = DiceEdit("drunk")
munchies_dice_edit = DiceEdit("munchies")
sweet_dice_edit = DiceEdit("sweet")
custom_dice_edit = DiceEdit("custom")
mystery_box_edit = DiceEdit("mystery")

# Preset Dice Options

sober_dice_edit.add_to_dice(["Italian", "Sushi", "Thai", "Mediterranean", "Ramen", "Tapas"])
drunk_dice_edit.add_to_dice(["Pizza", "Burger", "Burrito", "Brinner", "Grilled Cheese", "Nachos"])
munchies_dice_edit.add_to_dice(["French Fries", "Chips and Dip", "Everything in your fridge in a pan!", "Tacos", "Fried Egg Pizza Sandwich", "Cheesesteak"])
sweet_dice_edit.add_to_dice(["Candy!!", "Chocolate Raspberry Milk Shake", "Ice Cream!", "Cake", "CHOCOLATE", "Donuts"])

# Menu

print "Welcome to 'Hungry and Indecisive'! A set of food dice to make the decision a little easier!"



print "1 - Sober Dice"
print "2 - Drunk Dice"
print "3 - Munchies Dice"
print "4 - Sweet Dice"
print "5 - Custom Dice"
print "6 - Mystery Box Cooking Challenge"

# Choosing a dice

dice_choice = raw_input("Select the dice you would like to roll by typing the number on the menu:")
# dice_choice = int(dice_choice)

# Menu results in dice choice, leads you here:

# Sober

if dice_choice not in ["1", "2", "3", "4", "5", "6"] or dice_choice == "":
	print "You need to select an item from the menu! Type in the NUMBER on the menu that you would like choose."

elif dice_choice == 1:

	sober_greeting = random.choice(sober_witty_greeting)
	print sober_greeting

	yes_no = sober_dice_edit.yes_no_answer()
	sober_result = sober_dice_edit.random_outcome(yes_no)

	sober_result_reveal = random.choice(sober_witty_reveal)
	sober_result_ending = random.choice(sober_witty_ending)

	sober_string = sober_result_reveal + "\n" + sober_result + "\n" + sober_result_ending
	if yes_no == True:
		print sober_string
	# didn't like it? Want to roll again? Removes last rolled outcome.

# Drunk

elif dice_choice == 2:

	drunk_greeting = random.choice(drunk_witty_greeting)
	print drunk_greeting

	yes_no = drunk_dice_edit.yes_no_answer()
	drunk_result = drunk_dice_edit.random_outcome(yes_no)

	drunk_result_reveal = random.choice(drunk_witty_reveal)
	drunk_result_ending = random.choice(drunk_witty_ending)

	drunk_string = drunk_result_reveal + "\n" + drunk_result + "\n" + drunk_result_ending
	if yes_no == True:
		print drunk_string

# Munchies
		
elif dice_choice == 3:
	
	munchies_greeting = random.choice(munchies_witty_greeting)
	print munchies_greeting

	yes_no = munchies_dice_edit.yes_no_answer()
	munchies_results = munchies_dice_edit.random_outcome(yes_no)

	munchies_result_reveal = random.choice(munchies_witty_reveal)
	munchies_result_ending = random.choice(munchies_witty_ending)

	munchies_string = munchies_result_reveal + "\n" + munchies_results + "\n" + munchies_result_ending
	if yes_no == True:
		print munchies_string

# Sweet
		
elif dice_choice == 4:
	
	sweet_greeting = random.choice(sweet_witty_greeting)
	print sweet_greeting

	yes_no = sweet_dice_edit.yes_no_answer()
	sweet_results = sweet_dice_edit.random_outcome(yes_no)

	sweet_result_reveal = random.choice(sweet_witty_reveal)
	sweet_result_ending = random.choice(sweet_witty_ending)

	sweet_string = sweet_result_reveal + "\n" + sweet_results + "\n" + sweet_result_ending
	if yes_no == True:
		print sweet_string

# Custom

elif dice_choice == 5:
	print "So you can't decide what to eat, but you have a couple ideas! Let me help you with that!"
	print custom_dice_edit.custom_dice() # allows user to add custom outcomes
	yes_no = custom_dice_edit.yes_no_answer()
	custom_result = custom_dice_edit.random_outcome(yes_no) # creates random outcome
	custom_string = "Alright. Since you had some ideas, but didn't know what to do, the dice chose " + "\n" + custom_result + "\n" + "Now go do that. Also, you are a weird mix of decisive and indcecisive.  I approve."
	if yes_no == True:
		print custom_string

# MYSTERY BOX COOKING CHALLENGE
else: 
	print "Welcome to the Mystery Box Challenge! Roll the dice to find out what's in your Mystery Box!"
	yes_no = mystery_box_edit.yes_no_answer()
	mystery_box_results = mystery_box_roll() # formats the box items into a list
	mystery_box_string = "In your mystery box..." + "\n" + mystery_box_results + "Now get cooking!"
	if yes_no == True:
		print mystery_box_string


