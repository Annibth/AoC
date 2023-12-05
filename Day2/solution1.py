import csv

games = dict()
information = {"red": 12, "green":13, "blue": 14 }
possible = dict()

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day2/puzzle.csv") as file:
    reader = csv.reader(file, delimiter= ":")
    
    for row in reader:
        games[row[0]]= row[1]
    
for game in games:
    possible[game] = True
    games[game] = games[game].split(';')
    for i in range(len(games[game])):
        colours = games[game][i].split(',')
        games[game][i] = dict()
        for colour in colours:
            c = colour.split(' ')
            games[game][i][c[2]] = int(c[1])
            if (int(c[1])> information[c[2]]): possible[game] = False
s=0
for game in possible:
    if possible[game]: 
        print(f"GAME   A{game}")
        game=int(game.strip('Game '))
        print(f"GAME   B:{game}")
        s = s+game
print(s)