from DiceMainClass import *
from mystery_box import *
from diceRemarks import *

sober_dice_edit = DiceEdit("sober")
drunk_dice_edit = DiceEdit("drunk")
munchies_dice_edit = DiceEdit("munchies")
sweet_dice_edit = DiceEdit("sweet")
custom_dice_edit = DiceEdit("custom")
mystery_box_edit = DiceEdit("mystery")
cookie_dice_edit = DiceEdit("cookie")

# Preset Dice Options

sober_dice_edit.add_to_dice(["Italian Food, specifically Pasta!", "Sushi. Ask for Chef's Choice nigiri and see what you get!", "Thai Food!", "Mediterranean Food!", "Ramen, like real Ramen. Go to a restaurant!", "Tapas! Maybe a trip to Spain is in your future..."])
drunk_dice_edit.add_to_dice(["Pizza!", "Cheeseburger with fried pickles!", "Big Ass Burrito!", "Brinner (that's breakfast for dinner, for your drinking novices out there!", "Grilled Cheese with Hot Sauce!", "Nachos!!!!!"])
munchies_dice_edit.add_to_dice(["French Fries", "Chips and Dip: mouthfeel gets a solid 10!", "Everything in your fridge in a pan!", "Tacos! Tacos! Tacos!", "Fried Egg Pizza Sandwich", "Cheesesteak. Philly Cheesesteak!"])
sweet_dice_edit.add_to_dice(["Candy in a Cup!! Step 1: buy lots of candy. Step 2: Make a cup layered with candy. Step 3: EAT CANDY!", "Chocolate Raspberry Milk Shake with Extra Whipped Cream", "Ice Cream with Fudge Sauce!! And maybe a warm brownie?", "Your Favorite Flavor Cake", "CHOCOLATE", "Donuts"])
cookie_dice_edit.add_to_dice(["Chocolate Chip", "White Chocolate Chip", "Peanut Butter and Chocolate Chip"])

# Menu

print "Welcome to 'Hungry and Indecisive'! A set of food dice to make the decision a little easier!"

exit_flag = False

while exit_flag == False:

	print "1 - Sober Dice"
	print "2 - Drunk Dice"
	print "3 - Munchies Dice"
	print "4 - Sweet Dice"
	print "5 - Custom Dice"
	print "6 - Mystery Box Cooking Challenge"
	print "Type EXIT to stop rolling dice."

	# Choosing a dice

	dice_choice = raw_input("Select the dice you would like to roll by typing the number on the menu:")
	# dice_choice = int(dice_choice)

	# Menu results in dice choice, leads you here:



	if dice_choice not in ["1", "2", "3", "4", "5", "6", "7", "exit", "EXIT", "Exit"] or dice_choice == "" :
		print "\n \n" + random.choice(wrong_menu_response) + "\n \n"
	else:
		# EXIT
		if dice_choice in ["exit", "EXIT", "Exit"]:
			exit_flag == True
			exit_remark = random.choice(exit_witty_remark)
			print "\n \n" + exit_remark + "\n \n" 
			break

		# Sober

		elif dice_choice == "1":

			sober_greeting = random.choice(sober_witty_greeting)
			print "\n \n" + sober_greeting + "\n \n"

			yes_no = sober_dice_edit.yes_no_answer()
			sober_result = sober_dice_edit.random_outcome(yes_no)

			sober_result_reveal = random.choice(sober_witty_reveal)
			sober_result_ending = random.choice(sober_witty_ending)

			sober_string = "\n \n" + sober_result_reveal + "\n \n" + sober_result + "\n \n" + sober_result_ending + "\n \n"
			
			if yes_no == True:
				print sober_string

		# Drunk

		elif dice_choice == "2":

			drunk_greeting = random.choice(drunk_witty_greeting)
			print "\n \n" + drunk_greeting

			yes_no = drunk_dice_edit.yes_no_answer()
			drunk_result = drunk_dice_edit.random_outcome(yes_no)

			drunk_result_reveal = random.choice(drunk_witty_reveal)
			drunk_result_ending = random.choice(drunk_witty_ending)

			drunk_string = "\n \n" + drunk_result_reveal + "\n \n" + drunk_result + "\n \n" + drunk_result_ending + "\n \n"

			
			if yes_no == True:
				print drunk_string

		# Munchies
				
		elif dice_choice == "3":
			
			munchies_greeting = random.choice(munchies_witty_greeting)
			print "\n \n" + munchies_greeting

			yes_no = munchies_dice_edit.yes_no_answer()
			munchies_results = munchies_dice_edit.random_outcome(yes_no)

			munchies_result_reveal = random.choice(munchies_witty_reveal)
			munchies_result_ending = random.choice(munchies_witty_ending)

			munchies_string = "\n \n" + munchies_result_reveal + "\n \n" + munchies_results + "\n \n" + munchies_result_ending + "\n \n"
			
			if yes_no == True:
				print munchies_string

		# Sweet
				
		elif dice_choice == "4":
			
			sweet_greeting = random.choice(sweet_witty_greeting)
			print "\n \n" + sweet_greeting + "\n \n"

			yes_no = sweet_dice_edit.yes_no_answer()
			sweet_results = sweet_dice_edit.random_outcome(yes_no)

			sweet_result_reveal = random.choice(sweet_witty_reveal)
			sweet_result_ending = random.choice(sweet_witty_ending)

			sweet_string = "\n \n" + sweet_result_reveal + "\n \n" + sweet_results + "\n \n" + sweet_result_ending + "\n \n"
			
			if yes_no == True:
				print sweet_string

		# COOKIES

		elif dice_choice == "7":
		
			cookie_greeting = random.choice(cookie_witty_greeting)
			print "\n \n" + cookie_greeting + "\n \n"

			yes_no = cookie_dice_edit.yes_no_answer()
			cookie_results = cookie_dice_edit.random_outcome(yes_no)

			cookie_result_reveal = random.choice(cookie_witty_reveal)
			cookie_result_ending = random.choice(cookie_witty_ending)

			cookie_string = "\n \n" + cookie_result_reveal + "\n \n" + cookie_results + "\n \n" + cookie_result_ending + "\n \n"
				
			if yes_no == True:
				print cookie_string


		# Custom

		elif dice_choice == "5":
			
			custom_greeting = random.choice(custom_witty_greeting)
			print "\n \n" + custom_greeting

			print custom_dice_edit.custom_dice() # allows user to add custom outcomes
			
			yes_no = custom_dice_edit.yes_no_answer()
			custom_result = custom_dice_edit.random_outcome(yes_no) # creates random outcome
			
			custom_result_reveal = random.choice(custom_witty_reveal)
			custom_result_ending = random.choice(custom_witty_ending)

			custom_string = "\n \n" + custom_result_reveal + "\n \n" + custom_result + "\n \n" + custom_result_ending + "\n \n"

			if yes_no == True:
				print custom_string

		# MYSTERY BOX COOKING CHALLENGE
		else: 
			
			mystery_greeting = random.choice(mystery_witty_greeting)
			print "\n \n" + mystery_greeting + "\n \n"

			yes_no = mystery_box_edit.yes_no_answer()
			mystery_box_results = mystery_box_roll() # formats the box items into a list

			mystery_result_reveal = random.choice(mystery_witty_reveal)
			mystery_result_ending = random.choice(mystery_witty_ending)

			mystery_box_string = "\n \n" + mystery_result_reveal + "\n \n" + mystery_box_results + "\n \n" +mystery_result_ending + "\n \n"

			if yes_no == True:
				print mystery_box_string


