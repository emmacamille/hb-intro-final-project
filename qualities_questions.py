# questions about the qualities of foods

sobriety = raw_input("How sober are you? Type '1' for sober, '2' for drunk, and '3' for high as a kite:")
		#just want to save this data for the final outcome sentence


sweet_or_savory = raw_input("Are you looking for something sweet or savory? Type '1' for sweet and '0' for savory:") 

		if sweet_or_savory == 1:
			# go to sweet file
		else:
			# go to savory file

# could have another options that just states "fuck this!" which just picks a random option from either sweet or savory depending on last answer

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


