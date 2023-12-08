from enum import Enum

datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day8/puzzle.txt','r').read().split('\n\n')

rl = Enum('rl',['L','R'])

instructions = [rl[x].value-1 for x in datei[0]]
nodes = {x.split(' = ')[0].strip():[y.strip() for y in x.split(' = ')[1].strip('( )').split(',')] for x in datei[1].split('\n')}

start = 'AAA'
target = 'ZZZ'
steps = 0
found = False

while not found:
    for x in instructions:
        if start == target:
            print(steps)
            found = True
            break
        start = nodes[start][x]
        steps +=1
  