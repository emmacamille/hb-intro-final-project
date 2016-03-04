import random

mystery_box_categories = {
	"meat":["Pork Shoulder", "Beef Spare Ribs", "Talapia", "Whole Chicken", "Cornish Game Hens", "Duck Breast"],

	"veggie":["Collard Greens", "Brussels Sprouts", "Bok Choy", "Portobello Mushroom", "Asparagus", "Cabbage"],

	"starch":["Russet Potatos", "Lo Mein", "Basmati Rice", "Baguette", "Taro Root", "Garnet Yams"],

	"fruit":["Blueberries", "Avocado", "Tomato", "Strawberries", "Kumquat", "Orange"],

	"spice":["Turmeric", "Tomatillo", "Cumin", "Garamasala", "Paprika", "Jalepeno"]
}

mystery_box_results = []

for category in mystery_box_categories:
	result = random.choice(mystery_box_categories[category])
	mystery_box_results.append(result)

mystery_box_string = ""

for item in mystery_box_results:
	mystery_box_string = mystery_box_string + item + "\n"

print "In your mystery box..." + "\n" +mystery_box_string + "Now get cooking!"
