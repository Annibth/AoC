import csv
codes = list()
s= 0
config = list()
numbers= {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

with open(r"/Users/eliaruhle/Documents/Anna/AoC/AoC/Day1/puzzle.csv") as code:
    reader = csv.reader(code)

    for row in reader: 
        codes.append(row[0])
    
def indexes(element):
    return element[0]

def get_index(element,number):
    a=0
    index = list()
    while(a!=-1):
        if number in element:
            a = element.index(number)
            
            element = element.replace(number,numbers[number],1)
            index.append(a)
        else:
            a=-1
    return index
i=0
for element in codes:
    i+=1
    print(f"Before:{element}")
    done = False
    while not done:
        indices = []
        for number in numbers:
            index = get_index(element,number)
            for x in index:
                indices.append([x,number])
        #print(indices)
        if len(indices)!=0:
            indices.sort(key=indexes)
            #print(indices)
            element = element.replace(indices[0][1],numbers[indices[0][1]],1)
            print(element)
            if len(indices)>1:
                element = element.replace(indices[-1][1], numbers[indices[-1][1]])
        else:
            done = True
    print(f"After: {element}")
    element = [x for x in element if x.isdigit()]
    config.append(int(element[0]+ element[-1]))
    print(element[0]+ element[-1])
    if len(element)>1:
        s += int(element[0]+ element[-1])
    else:
        s += int(element[0])
        
all = []    
for i in range(0,len(codes)-1):
    all.append([codes[i],config[i]])

print(sum(config))
print(s)
