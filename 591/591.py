sets = {}
setNum = 0
averageHeight = 0

userInput = int(input())

while userInput != 0:
    numOfStacks = userInput
    words = input()
    stacks = []
    k = 0
    sum = 0

    for word in words.split():
        if word.isdigit():
            stacks.append(int(word))
            sum+= int(word)
    
    averageHeight = sum/numOfStacks         

    for stack in stacks:
        if stack > averageHeight:
            while(stack != averageHeight):
                stack-=1
        elif stack < averageHeight:
            while(stack != averageHeight):
                stack+=1
                k+=1

    userInput = int(input())
    setNum+=1
    sets[setNum] = k 

for item in sets:
    print("Set #" + str(item)) 
    print("The minimum number of moves is " + str(sets[item]) + ".\n")