def computePremium(numberOfFarmers):
    premium = 0
    for i in range(0, numberOfFarmers):
        userInput = input()
        numbers = []
        for word in userInput.split():
            if word.isdigit():
                numbers.append(int(word))

        sizeOfFarm = numbers[0]
        numberOfAnimals = numbers[1]
        enviFriendliness = numbers[2]

        premium += ((sizeOfFarm/numberOfAnimals) * enviFriendliness) * numberOfAnimals
    return int(premium)

numOfTestCases = int(input())
premiums = []
for item in range (0, numOfTestCases):
    premiums.append( computePremium(int(input())) )

for premium in premiums:
    print(premium)