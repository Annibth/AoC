import csv

cards = dict()
s = 0

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day4/puzzle.csv") as file:
    reader = csv.reader(file, delimiter= ":")
    
    for row in reader:
        index = int(row[0].strip('Card '))
        numbers = row[1].split('|')
        for n in numbers:
            new = n.strip()
            new = new.split(' ')
            numbers[numbers.index(n)]= [x for x in new if x]
        #matches
        numbers.append(0)
        #count
        numbers.append(1)
        cards[index]=numbers

print(cards)

for card in cards:
    print(cards[card])
    for number in cards[card][1]:
        if number in cards[card][0]: cards[card][2]= cards[card][2]+1
    j = cards[card][3]
    print(cards[card])
    while (j != 0):
        for i in range(1,cards[card][2]+1):
            cards[card+i][3]=cards[card+i][3]+1
            
        j-=1
    s = s+cards[card][3]
for card in cards.items():
    print(card)
    
print(s)