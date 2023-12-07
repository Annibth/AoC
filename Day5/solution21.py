translation = dict()
datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day5/puzzle.txt','r')
start = False
sections = datei.read().split('\n\n')

def dest(element):
    return(element[0])
  
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
actual_seeds= list()

seeds = [[x,seeds[seeds.index(x)+1]] for x in seeds if seeds.index(x)%2==0]
for x in seeds:
    while x[1]>0:
        x[1]-=1
        actual_seeds.append(x[0]+x[1])
        
print(len(actual_seeds))
min =0

while True:   
    removed = False    
    keys= [x for x in translation.keys()]
    keys.reverse()
    m = min
    for x in keys:
        for element in translation[x]:
            if m in range(element[0],element[0]+element[2]):
                m = element[1]+(m-element[0])
                break
    if m in actual_seeds:
        print(f"DONE: {min}")
        break
    min+=1