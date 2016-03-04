from DiceMainClass import *
from mystery_box import *

sober_dice_edit = DiceEdit("sober")
drunk_dice_edit = DiceEdit("drunk")
munchies_dice_edit = DiceEdit("munchies")
sweet_dice_edit = DiceEdit("sweet")

sober_dice_edit.add_to_dice(["Italian", "Sushi", "Thai", "Mediterranean", "Ramen", "Tapas"])
drunk_dice_edit.add_to_dice(["Pizza", "Burger", "Burrito", "Brinner", "Grilled Cheese", "Nachos"])
munchies_dice_edit.add_to_dice(["French Fries", "Chips and Dip", "Everything in your fridge in a pan!", "Tacos", "Fried Egg Pizza Sandwich", "Cheesesteak"])
sweet_dice_edit.add_to_dice(["Candy!!", "Chocolate Raspberry Milk Shake", "Ice Cream!", "Cake", "CHOCOLATE", "Strawberries"])

print "Welcome to 'Hungry and Indecisive'! A set of food dice to make the decision a little easier!"
print "1 - Sober Dice"
print "2 - Drunk Dice"
print "3 - Munchies Dice"
print "4 - Sweet Dice"
print "5 - Custom Dice"
print "6 - Myster Box Cooking Challenge"

dice_choice = raw_input("Select the dice you would like to roll by typing the number on the menu:")
dice_choice = int(dice_choice)

if dice_choice == 1:
	print "Awesome! You're sober and don't know what to eat, let me help you with that!"
	print sober_dice_edit.random_outcome()
	# didn't like it? Want to roll again? Removes last rolled outcome.

		
elif dice_choice == 2:
	print "NICE! You're drunk and don't know what to eat! Let me help you with that!"
	print drunk_dice_edit.random_outcome()
		
elif dice_choice == 3:
	print "DUDE! You're high and don't know what to eat! Let me help you with that!"
	print munchies_dice_edit.random_outcome()
		
elif dice_choice == 4:
	print "SWWEEEEETT! You're looking for something sweet and don't know what to eat! Let me help you with that!"
	print sweet_dice_edit.random_outcome()
	
elif dice_choice == 5:
	print "So you can't decide what to eat, but you have a couple ideas! Let me help you with that!"
	# need to add items to dice first then print random
	# automatically save dice to file
	# need to save name and food items
	print custom_dice_edit.random_outcome()

else: 
	print "Welcome to the Mystery Box Challenge! Roll the dice to find out what's in your Mystery Box!"

	mystery_box_string = mystery_box.myster_box_roll()

	print "In your mystery box..." + "\n" +mystery_box_string + "Now get cooking!"


