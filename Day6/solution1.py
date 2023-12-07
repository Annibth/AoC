datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day6/puzzle.txt','r')

races = [x.split(' ') for x in datei.read().split('\n')]
races = [[int(x) for x in races[0]if x.isdigit()], [int(x) for x in races[1] if x.isdigit()]]
races = [[races[0][i],races[1][i]] for i in range(0, len(races[0])) ]
print(races)

wins = 1

for x in races:
    win = 0
    for time in range(0,x[0]):
        distance = time * (x[0]-time)
        if distance>x[1]: win+=1
    wins= wins*win
        
print(wins)