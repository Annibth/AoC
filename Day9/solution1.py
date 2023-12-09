
datei = open('/Users/eliaruhle/Documents/Anna/AoC/AoC/Day9/puzzle.txt','r').read().split('\n')

data = [[int(y) for y in x.split(' ') if y !='']for x in datei]
data = [[[x[-1]],x] for x in data]
print(data)

s=0

for  element in data:
    current = element[1]
    while True:
        if set(current) == {0}:
            del data[data.index(element)][1]
            s += sum(data[data.index(element)][0])
            break
        else: 
            new = list()
            for i in range(0, len(current)-1):
                new.append(current[i+1]-current[i])
            current = new
            data[data.index(element)][0].append(new[-1])

print(s)           