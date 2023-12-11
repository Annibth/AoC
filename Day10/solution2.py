from enum import Enum
class Dir(Enum):
    I = [0,2]
    F = [1,2]
    N = [2,3]
    J = [3,0]
    X = [3,1]
    L = [0,1]
    O = [4,4]

def sort(element):
    return element[2]

map = open("/Users/eliaruhle/Documents/Anna/AoC/AoC/Day10/test2.txt","r").read().replace('|','I').replace('7','N').replace('-','X').replace('.','O').split('\n')
#print(map)
start = [[map.index(x), x.index('S')] for x in map if 'S'in x ][0]
current = [[start[0],start[1]+i,2+i] for i in (-1,1) if start[1]+i in range(0, len(map[start[0]]))]+[[start[0]+i,start[1],1-i] for i in (-1,1)if start[0] in range(0,len(map))]
current = [x for x in current if x[2]in Dir[map[x[0]][x[1]]].value]
loop = [[start, [x[0],x[1]]] for x in current]
loop[1].append(1)
count =1
#print(current)
former = [-1,-1,-1]
# node(x,y,ausbwelcher richtung kommend)
while True:
    if not current or  len(current)==1:
        break
    newc = list()
    for e in current:
        x=e[0]
        y=e[1]
        z=e[2]
        new = Dir[map[x][y]].value.copy()
        if z in new:
            new.remove(z)
            dir = new[0]
            element = [x+(-((dir+1)%2))**((dir+1)%3),y+(-(dir%2))**((dir+1)%3+((dir+1)%2)),(dir+2)%4]
            loop.append([[x,y],element[:2],count+1]) if newc  else loop.append([element[:2],[x,y]])
            if not newc or (newc[0][0],newc[0][1])!= (element[0],element[1]): newc.append(element)
        if former[0] == element[0] and former[1] == element[1]  :
            newc = []
            break
        else:
            former = element
    current = newc
    count+=1
    
print(count)
n = count
for i in range(0,len(loop),2):
    loop[i].append(count+n)
    n-=1
    
loop.sort(key = sort)
for l in loop:
    print(l)