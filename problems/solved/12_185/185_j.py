import sys
import time

lookup = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


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


def backTracking(node):
    global encodings, count
    if encodings > 1:
        return
    # if roman_letters['V'] == 8:
    #     print()
    if roman_letters[node] == 10:
        if node in [left1[0], left2[0], right[0]]:
            roman_letters[node] = 1
        else:
            roman_letters[node] = 0
        return
    node_value = roman_letters[node]
    roman_letters[node] = -1
    invalid_values = list(roman_letters.values())
    invalid_values = invalid_values[:invalid_values.index(-1)]
    roman_letters[node] = node_value

    #count += 1
    if node_value not in invalid_values:
        if node == letter_list[-1]:
            if testSum():
                encodings += 1
            roman_letters[node] += 1
            backTracking(node)
        else:
            # if roman_letters[node] == 9:
            #     if testMinRight(node):
            #         return
            if roman_letters[node] == 1:
                if testMaxRight():
                    return
            next_node = letter_list[letter_list.index(node) + 1]
            backTracking(next_node)
            roman_letters[node] += 1
            backTracking(node)
    else:
        roman_letters[node] += 1
        backTracking(node)


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
    left_sum = left1_value + left2_value
    if left_sum < min_right:
        return True
    else:
        return False


def testMaxRight():
    max_right = ((10 ** len(right)) - 1)
    if getLeftSum() > max_right:
        return True
    else:
        return False


def testSum():
    if getLeftSum() == getRightSum():
        return True
    else:
        return False


def getLeftSum():
    left1_value = ''
    for s in left1:
        left1_value += str(roman_letters[s])
    left1_value = int(left1_value)
    left2_value = ''
    for s in left2:
        left2_value += str(roman_letters[s])
    left2_value = int(left2_value)
    return left1_value + left2_value


def getRightSum():
    right_value = ''
    for s in right:
        right_value += str(roman_letters[s])
    return int(right_value)


st = ''
count = 0
encodings = 0
data = sys.stdin.read().split('\n')
#with open(r'C:\Users\jensm\Documents\GitHub\ap\Section 4\data.txt', 'r') as reader:
    #data = reader.read().split('\n')
#t = time.perf_counter()
for line in data[0:len(data)]:
    if line == '#':
        break
    left = line.split('=')[0]
    right = line.split('=')[1]
    left1 = left.split('+')[0]
    left2 = left.split('+')[1]

    romanSum()

    roman_letters = ''
    s = ''
    for i in range(9):
        if i < len(left1):
            s += left1[i]
        if i < len(left2):
            s += left2[i]
        if i < len(right):
            s += right[i]

    roman_letters = dict.fromkeys(s)
    for letter in roman_letters:
        roman_letters[letter] = 0
    roman_letters[left1[0]] = 1
    roman_letters[left2[0]] = 1
    roman_letters[right[0]] = 1
    letter_list = list(roman_letters.keys())

    #print(timeit.timeit('backTracking(left1[0])', globals=globals(), number=1))
    backTracking(left1[0])

    if encodings == 0:
        st += 'impossible\n'
       # print('impossible')
    if encodings == 1:
        st += 'valid\n'
        # print('valid')
    if encodings > 1:
        st += 'ambiguous\n'
        # print('ambiguous')
    encodings = 0
    
#print(time.perf_counter() - t)
#st[-1] = ''
print(st[:-1])
