from sys import stdin
calc_data = []

def calculate(b,p,m):
    return pow(int(b),int(p),int(m))

def process(line):
    calc_data.append(line)
    if len(calc_data) == 3:
        print(calculate(calc_data[0], calc_data[1], calc_data[2]))
        calc_data.clear()

for line in stdin:
    if line == '':
        break
    try:
        line = int(line)
        process(int(line))
    except ValueError:
        continue