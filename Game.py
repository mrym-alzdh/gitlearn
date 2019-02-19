import random

a = 1
b = 99
hads = random.randint(a,b)
print(hads)
javab = input()

while javab != "d":
    
    if javab == "k":
        b = hads-1
    elif javab == "b":
        a = hads+1
    
    hads = random.randint(a,b)
    print(hads)
    javab = input()

print("WOOOOOOW :))) I did it.")
