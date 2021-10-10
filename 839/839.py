tempStr = ""
numOfTests = int(input())
print("\n")


def checkIfEqual (string):

    arr = string.split(" ")
    leftSideWeight = int(arr[0])
    leftSideLength = int(arr[1])
    rightSideWeight = int(arr[2])
    rightSideLength = int(arr[3])
    
    leftForce = leftSideWeight * leftSideLength 
    rightForce = rightSideWeight * rightSideLength
    
    if leftSideWeight == 0:
        leftSideWeight = checkIfEqual(input())
    
    if rightSideWeight == 0:
        rightSideWeight = checkIfEqual(input())
    
    if (leftForce == rightForce) and (leftSideWeight != 0) and (rightSideWeight != 0):
        return leftSideWeight + rightSideWeight
    
    else:
        return 0


while numOfTests != 0:

    answer = False
    while(answer is False):
        userInput = input()
        if userInput == "":
            continue
        else:
            tempStr = ""
            answer = checkIfEqual(userInput)
            tempStr = ""

    print(str(answer) + "\n")
    answer = False
    numOfTests -= 1

print(tempStr)