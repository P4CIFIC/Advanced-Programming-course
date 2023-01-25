import sys
import time

# Assigns the numeric value of each Roman numeral
lookup = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


# Compares the sum of the left side of the equation with the right side of the equation 
# and assigns 'Correct' or 'Incorrect' to the global variable 'st'
def romanSum():
    global st
    left1_sum = 0
    for i in range(0, len(left1)):
        if i == len(left1) - 1:
            left1_sum += lookup[left1[i]]
        else:
            value = lookup[left1[i]]
            next_value = lookup[left1[i + 1]]
            if value < next_value:
                left1_sum -= value
            else:
                left1_sum += value

    left2_sum = 0
    for i in range(0, len(left2)):
        if i == len(left2) - 1:
            left2_sum += lookup[left2[i]]
        else:
            value = lookup[left2[i]]
            next_value = lookup[left2[i + 1]]
            if value < next_value:
                left2_sum -= value
            else:
                left2_sum += value

    right_sum = 0
    for i in range(0, len(right)):
        if i == len(right) - 1:
            right_sum += lookup[right[i]]
        else:
            value = lookup[right[i]]
            next_value = lookup[right[i + 1]]
            if value < next_value:
                right_sum -= value
            else:
                right_sum += value

    if left1_sum + left2_sum == right_sum:
        st += 'Correct '
        #print('Correct', end=' ')
    else:
        st += 'Incorrect '
        #print('Incorrect', end=' ')


# The main backtracking algorithm, it takes the current node as its input
def backTracking(node):
    global encodings, count
    # if the number of valid encodings is greater than one, return 
    if encodings > 1:
        return
    # if the current node is assigned the value of 10, change it to 1 or 0 based on the position of the node in the equation
    if roman_letters[node] == 10:
        if node in [left1[0], left2[0], right[0]]:
            roman_letters[node] = 1
        else:
            roman_letters[node] = 0
        return
    node_value = roman_letters[node]
    roman_letters[node] = -1
    # create a list of invalid values based on the current assignments of the nodes
    invalid_values = list(roman_letters.values())
    invalid_values = invalid_values[:invalid_values.index(-1)]
    roman_letters[node] = node_value

    # if the current value of the node is not in the list of
    # invalid values, proceed to the next node
    if node_value not in invalid_values:
        if node == letter_list[-1]:
            # if the current node is the last node, check if the equation is true
            if testSum():
                encodings += 1
            roman_letters[node] += 1
            backTracking(node)
        else:
            # if the current node is not the last node, call the function recursively on the next node
            # then increment the current node by 1 and call the function recursively again on the current node
            next_node = letter_list[letter_list.index(node) + 1]
            backTracking(next_node)
            roman_letters[node] += 1
            backTracking(node)
    else:
        # if the current value of the node is in the list of invalid values, increment the value by 1 and call the function recursively on the current node
        roman_letters[node] += 1
        backTracking(node)
        
# function used to check if the maximum possible value of the right side of the equation is less than the left side of the equation to stop the backtracking early
def testMaxRight():
    max_right = (10 ** (len(right) - 1)) - 1
    left1_value = ''
    for s in left1:
        left1_value += str(roman_letters[s])
    left1_value = int(left1_value)
    left2_value = ''
    for s in left2:
        left2_value += str(roman_letters[s])
    left2_value = int(left2_value)
    if left1_value + left2_value >= max_right:
        return True
    return False

# function used to check if the minimum possible value of the right side of the equation is less than the left side of the equation to stop the backtracking early
def testMinRight(node):
    min_right = (10 ** (len(right) - 3))
    left1_value = ''
    found = False
    for s in left1:
        if s == node:
            found = True
        if not found:
            left1_value += str(roman_letters[s])
        else:
            left1_value += '9'
    left1_value = int(left1_value)
    left2_value = ''
    found = False
    for s in left2:
        if s == node:
            found = True
        if not found:
            left2_value += str(roman_letters[s])
        else:
            left2_value += '9'
    left2_value = int(left2_value)
    if left1_value + left2_value <= min_right:
        return True
    return False

encodings = 0

st = ''

line = input()

while line != "":
    letter_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = 0
    left1 = line[:line.index('+') - 1]
    left2 = line[line.index('+') + 2:line.index('=') - 1]
    right = line[line.index('=') + 2:]
    for s in left1:
        if s not in letter_list:
            letter_list.append(s)
            roman_letters[s] = 0
    for s in left2:
        if s not in letter_list:
            letter_list.append(s)
            roman_letters[s] = 0
    for s in right:
        if s not in letter_list:
            letter_list.append(s)
            roman_letters[s] = 0
    start_time = time.time()
    backTracking(letter_list[0])
    romanSum()
    print(st, end=' ')
    print('%.6f' % (time.time() - start_time))
    line = input()
