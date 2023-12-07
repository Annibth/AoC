datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day6/puzzleg.txt','r')

race = [int(x.strip(' Time:Dstanc').replace(' ','')) for x in datei.read().split('\n')]
print(race)


wins = 0

for time in range(0,race[0]):
    distance = time * (race[0]-time)
    if distance>race[1]: wins+=1

    
print(wins)