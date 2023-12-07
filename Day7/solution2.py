import csv
from enum import Enum

hands = {1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
ranking = []

cards = Enum('Card',['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])
type = Enum('Type',['HIGH','ONEPAIR', 'TWOPAIR','THREE','FULLHOUSE','FOUR', 'FIVE' ])

def sort_cards(element):
    values = []
    for x in element[0]:
        values.append(cards[x].value)
    return values

def get_type(element):
    counts= list()
    jokers=0
    for x in element:
        if x == 'J':
            jokers+=1
        else:
            counts.append(element.count(x))
    counts.sort(reverse = True)
    print(counts)
    if counts: jokers =counts[0]+jokers
    if jokers >= 3:
        if jokers == 5:
            return type.FIVE.value
        elif jokers == 4:
            return type.FOUR.value
        elif counts[-1]== 2:
            return type.FULLHOUSE.value
        return type.THREE.value
    else:
        if jokers == 2:
            if counts[2] == 2:
                return type.TWOPAIR.value
            return type.ONEPAIR.value
        return type.HIGH.value
            
            

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day7/puzzle.csv") as file:
    reader = csv.reader(file, delimiter=' ')
    
    for row in reader:
        rank = get_type(row[0])
        
        hands[rank].append(row)


for t in hands:
    hands[t].sort(key= sort_cards, reverse = True)
    ranking.extend(hands[t])

total = 0
for i in range(0,len(ranking)):
    print(f"RANG:{i}\n BID: {ranking[i][1]}")
    total = total + (int(ranking[i][1])*(i+1))
    
print(total)
    