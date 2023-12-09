from enum import Enum
import math

datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day8/puzzle.txt','r').read().split('\n\n')

rl = Enum('rl',['L','R'])

instructions = [rl[x].value-1 for x in datei[0]]
nodes = {x.split(' = ')[0].strip():[y.strip() for y in x.split(' = ')[1].strip('( )').split(',')] for x in datei[1].split('\n')}

start = [x for x in nodes if x[2]=='A']
print(start)
target = [x for x in nodes if x[2]=='Z']
print(target)
steps = 1
found = False

def kgV(list):
    for i in range(0,len(list)):
        print(list[0])
        list[0]=math.lcm(list[0],list[i])
    return list[0]
        

while not found:
    for x in instructions:
        print(start)
        if [x for x in start if not x.isdigit()]:
            for node in start:
                if not node.isdigit():
                    current = nodes[node][x]
                    if current[2]=='Z':
                        start[start.index(node)] = str(steps)
                    else:
                        start[start.index(node)] = nodes[node][x]
            start = list(set(start))
            steps +=1
        else:  
            print(start)
            s = kgV([int(x) for x in start])
            print(s)
            found = True
            break
        