def calculate(b,p,m):
    return pow(int(b),int(p),int(m))

final = []

while True:
    try:
        final.append(input())
        if len(final) == 3:
            print(calculate(final[0], final[1], final[2]))
            final.clear()
    except EOFError:
        break