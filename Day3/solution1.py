import csv
import string
import re

scheme = list()
lines = list()
symbols = string.punctuation
print(symbols)
s =0

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day3/puzzle.csv") as file:
    reader = csv.reader(file)
    
    for row in reader:
        scheme.append(row[0])

for line in scheme:
    l = line
    for symbol in symbols:
        l = l.replace(symbol,'.')
    li = l.split('.')
    li = [[x] for x in li if x.isdigit()]
    for i in range(0,len(li)):
        print(li[i][0])
        li[i].append(l.index(li[i][0]))
        dots= "."*len(li[i][0])
        l=l.replace(li[i][0],dots,1)
    for x in range(0,len(li)):
        indices = list()
        for i in range(0,len(li[x][0])):
            indices.append(li[x][1]+i)
        lines.append([scheme.index(line),li[x],indices])


neighbours = list()

for line in lines:
    neighbour = list()
    side = [max(min(line[2])-1,0),min(max(line[2])+1,len(scheme[line[0]])-1)]
    for x in line[2]:
        if line[0]>0: neighbour.append(scheme[line[0]-1][x])
        if line[0]<len(scheme)-1:neighbour.append(scheme[line[0]+1][x])
    for x in side:
        neighbour.append(scheme[line[0]][x])
        if line[0]>0:neighbour.append(scheme[line[0]-1][x])
        if line[0]<len(scheme)-1:neighbour.append(scheme[line[0]+1][x])
    neighbours.append([line[1],[x for x in neighbour if x !='.' and not x.isdigit()]])
    
   
#print(neighbours) 
for number in neighbours:
    if number[1] : 
        #print(number[0])
        s = s+int(number[0][0])
        
print(f"SUMME: {s}")

#525008