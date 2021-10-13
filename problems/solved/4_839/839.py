def checkIfEqual (string):
    arr = string.split(" ")

    leftSideWeight = int(arr[0])
    leftSideLength = int(arr[1])
    rightSideWeight = int(arr[2])
    rightSideLength = int(arr[3])
    
    if leftSideWeight == 0:
        leftSideWeight = checkIfEqual(input())
    
    if rightSideWeight == 0:
        rightSideWeight = checkIfEqual(input())
    
    leftForce = leftSideWeight * leftSideLength 
    rightForce = rightSideWeight * rightSideLength
    
    if (leftForce == rightForce) and (leftSideWeight != 0) and (rightSideWeight != 0):
        return leftSideWeight + rightSideWeight
    
    else:
        return 0

numOfTests = int(input())
input()
remaining = 0
output = ""

while remaining < numOfTests:
    
    answer = checkIfEqual(input())

    if remaining != (numOfTests - 1):

        if answer == 0:
            output += "NO\n\n"
            input()
        else:
            output += "YES\n\n"
            input()
    else:

        if answer == 0:
            output += "NO"
        else:
            output += "YES"
        
    remaining += 1

print(output)