numOfTests = int(input())
print("\n\n")
wL = ""
dL = ""
wR = ""
dR = ""
array = []
dict = {}
tempStr = []
counter = 1

userInput = input()
tempStr = ""
for line in userInput:
    if line.isdigit():
        tempStr += line
    
dict["L"+str(counter)] = tempStr[0:2]
dict["R"+str(counter)] = tempStr[2:4]

print(dict["L" + str(counter)][0])
print(dict["R" + str(counter)][0])

while(1):
    userInput = input()
    tempStr = ""
    for line in userInput:
        if line.isdigit():
            tempStr += line
    counter += 1
    dict["L"+str(counter)] = tempStr[0:2]
    dict["R"+str(counter)] = tempStr[2:4]
    
    if (tempStr[0] and tempStr[2]) == 0:
        addLeft()
        addRight()
    elif tempStr[0] == 0:
        addLeft()
    elif tempStr[2] == 0:
        addRight()
    else:
        

    #if (dict["L" + str(counter)][0] or dict["R" + str(counter)][0]) == '0':

    
print(array)

def addRight():
    if (tempStr[0]) == 0:
        n = counter
        n += 1

def addLeft():


        