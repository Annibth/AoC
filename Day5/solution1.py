translation = dict()
datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day5/puzzle.txt','r')
start = False
sections = datei.read().split('\n\n')
    
for section in sections:
    configs=list()
    new = section.split('\n')
    for number in new:
        element= number.split(' ')
        if not element[0].isdigit():
            if element[0] == "seeds:":
                configs = [int(x) for x in element[1:]]
                start=True
            else:
                header = element[0].split('-')
        else: 
            configs.append([int(x) for x in element])
    if start: 
        seeds =  configs
        start = False
    else:
        translation[header[0]]=configs

locations = list()
found = False

for seed in seeds:
    x = int(seed)
    for element in translation:
        print(f"ELEMENT:{element}")
        for number in translation[element]:
            print(f"NUMBER: {number}")
            if x in range(number[1], number[1]+number[2]):
                print(f"SOURCE:{element}{x}")
                x = int(number[0])+(x-number[1])
                found = True
                print(f"DESTINATION:{x}")
                break
    locations.append(x)                    

print(min(locations))