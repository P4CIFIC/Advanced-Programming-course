import sys

def solve(s , t):
    counter = 0
    head = 0
    for i in range (len(s)):
        char = s[i]
        for j in range(head, len(t)):
            if  char == t[j]:
                counter += 1
                head = j + 1
                break
    if counter == len(s):
        return "Yes"
    return "No"

for line in sys.stdin:
    if line == '':
        break
    line = line.split()
    s = line[0]
    t = line[1] 
    print(solve(s,t))