#Final Project

#I'm Hungry and Indecisive... what should I eat?

So you don't know what to eat? I see... Let me ask you a couple of questions to eliminate some options and then you can either see our list or choose to "Roll the dice" and get a random option.

Happy eating!

#User Flow:

- Sobriety Options
- Answer 5 questions about the qualities of food the user is looking for:
	- Hot or Cold
	- Sweet or Savory
	- Chewy or Crunchy
	- Utensils or None
	- Healthy or Not
- Either select to see options or "Roll the Dice"
- Get eating!

#Psuedocode:

- A list of lists/dictionaries will hold the possible outcomes and the qualities that are associated with them.

- The user questions will be if/else statements that will eliminate options from the main list of outcomes.

- The outcomes will either be printed at the user's request or one outcome will be printed at random by "rolling the dice".

- At any point during the qualities questions, the user could type "fuck this" and the program will just print a random outcome based on their most recent answer.

Skills used: lists, dictionaries, modules, conditionals.

Questions about the qualities of foods

sobriety = raw_input("How sober are you? Type '1' for sober, '2' for drunk, and '3' for high as a kite:")
		#just want to save this data for the final outcome sentence


sweet_or_savory = raw_input("Are you looking for something sweet or savory? Type '1' for sweet and '0' for savory:") 

		if sweet_or_savory == 1:
			# go to sweet file
		else:
			# go to savory file

Could have another options that just states "fuck this!" which just picks a random option from either sweet or savory depending on last answer

hot_or_cold = raw_input("Are you in the mood for hot or cold food? Type '1' for hot and '0' for cold:")
		
		if hot_or_cold == 1:
			# remove all items with 'cold' as a quality
		else:
			# remove all items with 'hot' as a quality

chewy_or_crunchy = raw_input("Do you want food that is chewy or crunchy? Type '1' fo chewy and '0' for crunchy:")
		
		if chewy_or_crunchy == 1:
			# remove all items with 'crunchy' as a quality
		else:
			# remove all items with 'chewy' as a quality'

utensils_or_none = raw_input("Do you want to eat with utensils or with your hands, like a barbarian? Type '1' for utensils and '0' for none:")
		
		if utensils_or_none == 1:
			# remove all items with 'no utensils' as a quality
		else:
			# remove all items with 'utensils' as a quality

healthy_or_not = raw_input("Are you trying to stay healthy here or do you not care? Type '1' for healthy and '0' for not caring:")
		
		if healthy_or_not == 1:
			# remove all items with 'cold' as a quality
		else:
			# remove all items with 'hot' as a quality




