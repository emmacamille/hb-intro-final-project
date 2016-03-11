from DiceMainClass import *
from mystery_box import *

sober_dice_edit = DiceEdit("sober")
drunk_dice_edit = DiceEdit("drunk")
munchies_dice_edit = DiceEdit("munchies")
sweet_dice_edit = DiceEdit("sweet")
custom_dice_edit = DiceEdit("custom")

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
dice_choice = int(dice_choice)

# Menu results in dice choice, leads you here:

# Sober

if dice_choice == 1:
	print "Being sober isn't the end of the world.  But you can't decide on what to eat! Hmmmm... sucks for you! Wait! Let me help you with that!"
	sober_result = sober_dice_edit.random_outcome()
	print "You're sober... so... you should eat...." + "\n" + sober_result + "\n" + "Now get eating!!!"
	# didn't like it? Want to roll again? Removes last rolled outcome.

# Drunk

elif dice_choice == 2:
	print "NICE! You're drunk and don't know what to eat! Let me help you with that!"
	drunk_result = drunk_dice_edit.random_outcome()
	print "Since you're drunk... you should definitely eat...." + "\n" + drunk_result + "\n" + "Now get eating!!! Oh, and have another drink for me, would'ya?"

# Munchies
		
elif dice_choice == 3:
	print "Excellent maaaaaannn! You're high and don't know what to eat! Let me help you with that!"
	munchies_results = munchies_dice_edit.random_outcome()
	print "While you're high... you should get down on...." + "\n" + munchies_results + "\n" + "Now get munchin'!!!"

# Sweet
		
elif dice_choice == 4:
	print "SWWEEEEETT! You're looking for something sweet and don't know what to eat! Let me help you with that!"
	sweet_results = sweet_dice_edit.random_outcome()
	print "Your sweet tooth saver should be..." + "\n" + sweet_results + "\n" + "MMmmmmmm... so sweeet!"
# Custom

elif dice_choice == 5:
	print "So you can't decide what to eat, but you have a couple ideas! Let me help you with that!"

	print custom_dice_edit.custom_dice() # allows user to add custom outcomes

	print custom_dice_edit.random_outcome() # creates random outcome

# MYSTERY BOX COOKING CHALLENGE
else: 
	print "Welcome to the Mystery Box Challenge! Roll the dice to find out what's in your Mystery Box!"

	mystery_box_string = mystery_box_roll() # formats the box items into a list

	print "Are you ready to roll the dice?"
	yes_no_answer = raw_input("Yes or no?")

	if yes_no_answer == "NO" or yes_no_answer == "no" or yes_no_answer == "No" or yes_no_answer == "n" or yes_no_answer == "N":
		print "What?! And miss out on the fun! Fine. Be that way."

	else: 
		print "In your mystery box..." + "\n" + mystery_box_string + "Now get cooking!"


