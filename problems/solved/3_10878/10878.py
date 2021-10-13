bytes = []
tempList = []
tempList2 = []

userInput = input()

# saving raw input in array line by line
while True:
    userInput = input()
    if (userInput == "___________") and (len(tempList) > 0):
        break
    else:
        for item in userInput.split("|"):
            tempList.append(item)

# formatting the array of raw input and removing empty elements and dots in array.
# then replacing all "o" with "1" and the corresponding for spaces as "0"
tempList2 = [s.replace("o", "1") for s in [s.replace(".", "") for s in list(filter(None, tempList))]]
bytes = [s.replace(" ", "0") for s in tempList2]

##Iterating through array of bytes and converting these to their corresponding ASCII value
ascii_str = ""
for binary_value in bytes:
    an_integer = int(binary_value, 2)
    ascii_char = chr(an_integer)
    ascii_str += ascii_char

#problem in onlinejudge causing issues in output formatting. Therefore...
print (ascii_str, end="")