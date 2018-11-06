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

rooms = []
d = []
maxlines = 18
maxchars = 70
minrooms = 0
maxrooms = 0

for y, line in enumerate(range(maxlines)):
    l = []
    #if line == 0 or line == 1 or line == 2 or line == 3 or line == 4 or line == 5 or line == 6 or line == 7 or line == 8 or line == 9:
    for x, char in enumerate(range(maxchars)):
        if x == 0 or x == maxchars-1 or y == 0 or y == maxlines-1:
            l.append("#")
        #l.append(random.choice(list(legend.keys())))
        else:
            l.append(random.choice(("#")))
            
    d.append(l)
    
# ---- snake ----

y = random.randint(1, maxlines-2)
for x in range(1, maxchars-1):
	d[y][x] = "."
	if random.random() > 0.8:
		# i want to go deeper
		howmuch = random.randint(1, 7)
		if y + howmuch < maxlines-2:
			for _ in range(howmuch):
			    y += 1
			    d[y][x] = "."
	elif random.random() < 0.2:
		# i want to go higher
		howmuch = random.randint(1, 7)
		if y - howmuch > 1:
			for _ in range(howmuch):
				y -= 1
				d[y][x] = "."
# ---- create rooms ----

#for r in range(random.randint(minrooms, maxrooms)):
#    # linke obere ecke, x coordinate
#    x = random.randint(1, maxchars-10)
#    # linke obere ecke, y coordinate
#    y = random.randint(1, maxlines-5)
#    # raumbreite
#    b = random.randint(1, 8)
#    # raumhöhe
#    h = random.randint(1, 3)
#    rooms.append((x, y, b, h))
    
# ---- carve out rooms ----

#for r in rooms:
#   x1 , y1, b, h = r
#   for y, line in enumerate(d):
#       for x, char in enumerate(line):
#           if y >= y1 and y <= y1+h and x >= x1 and x <= x1+ b:
#               d[y][x] = "." 

    
# ---- dungeon printer ----

for l in d:
    for char in l:
        print(char, end="")
    print()
    
#print(rooms)
        

