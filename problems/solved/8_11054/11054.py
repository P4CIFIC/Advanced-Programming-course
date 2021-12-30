lines = []

while True:
    line = input()
    try:
        end = int(line)
        if end == 0:
            break
        else:
            lines.append(line)
    except ValueError:
        lines.append(line)
        continue

def solve(number_of_houses, houses):
    number_of_steps = 0
    for i in range(number_of_houses):
        if houses[i] == 0:
            continue
        payload = houses[i]
        number_of_steps += abs(payload)
        houses[i + 1] += payload
    return number_of_steps
            
while lines:
    houses = []
    number_of_houses = int(lines.pop(0))
    for word in lines.pop(0).split():
        houses.append(int(word))
    print(solve(number_of_houses, houses))