import random

legend = {".": {"name": "floor",
                "prob": 0.1},
          "b": {"name": "bush",
				"prob": 0.02},
		  "#": {"name": "rock",
				"prob": 0.01},				
		  "d": {"name": "door",
			    "prob": None},
		  "<": {"name": "stair down",
				"prob": None},
		  ">": {"name": "stair up",
				"prob": None}
		 }

d = []
maxlines = 10
maxchars = 30

for y, line in enumerate(range(maxlines)):
	l = []
	#if line == 0 or line == 1 or line == 2 or line == 3 or line == 4 or line == 5 or line == 6 or line == 7 or line == 8 or line == 9:
	for x, char in enumerate(range(maxchars)):
		if x == 0 or x == maxchars-1 or y == 0 or y == maxlines-1:
			l.append("#")
		#l.append(random.choice(list(legend.keys())))
		else:
			l.append(random.choice((".", ".", ".", ".", ".", ".", ".", ".", "b", "#", "#")))
			
	d.append(l)
	
#---- dungeon printer ----

for l in d:
	for char in l:
		print(char, end="")
	print()
	

		

