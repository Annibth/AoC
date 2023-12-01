import csv
codes = list()
s= 0

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day1/puzzle.csv") as code:
    reader = csv.reader(code)

    for row in reader: 
        codes.append(row[0])

for element in codes:
    element = [x for x in element if x.isdigit()]
    s += int(element[0]+ element[-1])
    
print(s)
