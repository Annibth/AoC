def f (x):
    return (-(x%2))**((x+1)%3+((x+1)%2))

print(f(0))
print(f(1))
print(f(2))
print(f(3))

#0- 1,2,3
#1- 2,0
#2- 1,2,3
#3- 1,3