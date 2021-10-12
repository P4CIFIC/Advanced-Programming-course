def checkIfEqual (string):
    if string == "":
        string = checkIfEqual(input())
    else:
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

numOfTests = int(input())
#print("\n")

while numOfTests != 0:
    answer = ""
    
    while(answer is False):
        answer = checkIfEqual(input())

        if answer == 0:
            

    print(str(answer) + "\n")
    answer = False
    numOfTests -= 1
