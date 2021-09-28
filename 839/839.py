numOfTests = int(input())
print("\n")

areEqual = False
offsetRightSides = 0
tempStr = ""
leftSides = []
rightSides = []
flipFlop = True
"""
def checkIfEqual (counterLeft, counterRight, string):
    oneInput = list(string)
    leftSideWeight = int(oneInput[0])
    leftSideLength = int(oneInput[1])
    rightSideWeight = int(oneInput[2])
    rightSideLength = int(oneInput[3])
    
    if counterLeft != 0:
    
        if leftSideWeight != 0:
            leftSides.append(leftSideWeight)
            counterLeft -= 1
        else:
            counterLeft += 1
        
        if rightSideWeight != 0:
            leftSides.append(rightSideWeight)
            counterLeft -= 1
        else:
            counterLeft -= 1


    if counterRight != 0:
    
        if leftSideWeight != 0:
            rightSides.append(leftSideWeight)
            counterRight -= 1
        else:
            counterRight += 1
        
        if rightSideWeight != 0:
            rightSides.append(rightSideWeight)
            counterRight -= 1
        else:
            counterRight -= 1

    for leftMass in leftSides:
        leftSideWeight = 0
        leftSideWeight += leftMass
    for rightMass in rightSides:
        rightSideWeight = 0
        rightSideWeight += leftMass

    if (leftSideWeight*leftSideLength) == (rightSideWeight*rightSideLength):
        return "YES"
    else:
        return "NO"
"""


while numOfTests != 0:
    answer = False
    while(answer is False):
        userInput = input()
        tempStr = ""
        for line in userInput:
            if line.isdigit():
                tempStr += line            
        
        answer = checkIfEqual( 1, 1, tempStr)
        tempStr = ""
        leftSides = []
        rightSides = []
    print(answer + "\n")
    answer = False
    numOfTests -= 1

print(tempStr)
