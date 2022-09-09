player_names = ["Magnus Carlsen", "Fabiano Caruana", "Yifan Hou", 
"Wenjun Ju"]

fixtures = [(f'{x} versus {y}') for x in player_names for y in player_names if x != y ]

print(fixtures)