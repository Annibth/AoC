import csv

cards = list()
s = 0

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day4/puzzle.csv") as file:
    reader = csv.reader(file, delimiter= ":")
    
    for row in reader:
        numbers = row[1].split('|')
        for n in numbers:
            new = n.strip()
            new = new.split(' ')
            numbers[numbers.index(n)]= [x for x in new if x]
        numbers.append(0.5)
        cards.append(numbers)

for card in cards:
    for number in card[1]:
        if card[1].count(number)>=2: print("DOUBLE")