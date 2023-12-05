import csv
codes = list()
s= 0
config = list()
numbers= {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day1/puzzle.csv") as code:
    reader = csv.reader(code)

    for row in reader: 
        codes.append(row[0])

for element in codes:
    element = [x for x in element if x.isdigit()]
    print(element)
    print(element[0]+ element[-1])
    s += int(element[0]+ element[-1])

print(s)
