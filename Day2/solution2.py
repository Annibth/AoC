import csv

games = dict()
minimum = dict()
s = 0

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day2/test.csv") as file:
    reader = csv.reader(file, delimiter= ":")
    
    for row in reader:
        games[row[0]]= row[1]
    
for game in games:
    minimum[game] = dict()
    games[game] = games[game].split(';')
    for i in range(len(games[game])):
        colours = games[game][i].split(',')
        games[game][i] = dict()
        for colour in colours:
            c = colour.split(' ')
            if c[2] in minimum[game]:
                minimum[game][c[2]].append(int(c[1]))
            else: 
                minimum[game][c[2]]=[int(c[1])]

for game in minimum:
    power = 1
    for colour in minimum[game]:
        power = power * max(minimum[game][colour])
    s = s+power  
print(s)
    