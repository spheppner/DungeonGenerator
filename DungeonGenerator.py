import random

legend = {".": {"name": "floor",
                "prob": None},
          "b": {"name": "bush",
                "prob": 0.02},
          "#": {"name": "rock",
                "prob": 0.6},              
          "d": {"name": "door",
                "prob": None},
          "<": {"name": "stair down",
                "prob": 0.02},
          ">": {"name": "stair up",
                "prob": 0.02}
         } 
         
rooms = []
d = []
ft = 1
et = 1
rt = 1
maxlines = 18
maxchars = 70
maxrooms = 4
maxstairs = 4
maxrocks = 30
room_nr = 0
stair_nr = 0
rock_nr = 0
stairdown_prob = legend["<"]["prob"]
stairup_prob = legend[">"]["prob"]
bush_prob = legend["b"]["prob"]
rock_prob = legend["#"]["prob"]

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
    # ---- new room? ----
    elif rt == 1:
        rt = 0
        room_nr += 1
        maxbreite = maxchars-2 - x
        b = min(random.randint(3, 15), maxbreite)
        maxtiefe = maxlines-2 - y
        h = min(random.randint(2, 10), maxtiefe)
        rooms.append((x, y, b, h))
    elif random.random() < 0.1 and room_nr < maxrooms:
        room_nr += 1
        maxbreite = maxchars-2 - x
        b = min(random.randint(3, 15), maxbreite)
        maxtiefe = maxlines-2 - y
        h = min(random.randint(2, 10), maxtiefe)
        rooms.append((x, y, b, h))
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

for r in rooms:
    x1 , y1, b, h = r
    for y, line in enumerate(d):
        for x, char in enumerate(line):
            if y >= y1 and y <= y1+h and x >= x1 and x <= x1+ b:
                d[y][x] = "."     
#                if ft == 1:
#                    ft = 0
#                    d[y][x] = "<"     
#                elif random.random() < stairdown_prob and stair_nr < maxstairs:
#                    stair_nr += 1
#                    d[y][x] = "<"
#                elif et == 1:
#                    et = 0
#                    d[y][x] = ">"
#                elif random.random() < stairup_prob and stair_nr < maxstairs:
#                    stair_nr += 1
#                    d[y][x] = ">"
                if random.random() < rock_prob:
                    if rock_nr < maxrocks and y > y1 and y < y1+ h and x > x1 and x < x1+b:
                        rock_nr += 1
                        d[y][x] = "#"
                 
# treppenschleife

pebbles = []
for y, line in enumerate(d):
    for x, char in enumerate(line):
        if d[y][x] == ".":
            pebbles.append((x,y))

random.shuffle(pebbles)
max_pebbles = len(pebbles)
n = 0
x = pebbles[n][0]
y = pebbles[n][1]
d[y][x] = "<"
n = 1
x = pebbles[n][0]
y = pebbles[n][1]
d[y][x] = ">"
for n in range(2, random.randint(1, max_pebbles)):
    x = pebbles[n][0]
    y = pebbles[n][1]
    if random.random() < stairdown_prob:
        d[y][x] = "<"
    elif random.random() < stairup_prob:
        d[y][x] = ">"


# ---- dungeon printer ----

for l in d:
    for char in l:
        print(char, end="")
    print()    
#print(rooms)

print(max_pebbles)
