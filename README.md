#Final Project

#I'm Hungry and Indecisive... what should I eat?

Here you can "roll the dice" for ideas on what your next meal should include. Currently, there are preprogrammed dice you can choose from: Sober, Drunk, Munchies, Sweet, Custom or take on a Mystery Box Challege.

Once the category is selected, the computer "rolls the dice".
 
#User flow: 

Run the program.

A menu will appear with the following options:
	
	Choose how sober you are:
		- Straight Edge
		- Druuuunk
		- MUNCHIES!!!!
		- Sweet
		- Custom
		- Mystery Box Cooking Challenge

Once the dice has been chosen:
	
	You selected (name of dice), are you ready to roll? 'Yes' or 'No'

	If 'Yes':
		print "Alright! Here goes! You should (cook/eat(depending on dice selection))..."

	elif 'No':
		print "Really? You're that indecisive? Fine!"

If the Mystery Box Cooking Challenge is selected, the user will be offered 5 outcomes: meat, veggie, starch, fruit and spice. These outcomes will result in a "shopping list" and the challenge is to make a meal with these items as a base.

#Psuedocode

1. Set of functions within a class in order to manipulate the dice.
	- Add food item to dice
	- Remove food item from dice
	- Choose random food from dice
	- Return list of outcomes
	- Save custom dice input
	- Read customized die

2. Create pre-set dice options.
	- Sober, drunk, munchies and sweet.

3. Create dice customization option

4. Create Mystery Box Challenge
	- Contains 5 categories of food: meat, veggie, starch, fruit and spice.
	- Prints out a random choice from each option.