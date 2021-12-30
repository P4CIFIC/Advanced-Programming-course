def solve(n, k):
    arr = [[i for i in range(k + 1)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, k + 1):
            arr[i][j] = arr[i -1][j] + arr[i][j - 1]
    return arr[n - 1][k] % 1000000

lines = []
while True:
    line = input()
    try:
        if line == "0 0":
            break
        else:
            lines.append(line)
    except ValueError:
        lines.append(line)
        continue

for line in lines:
    temp = line.split()
    n = int(temp[0])
    k = int(temp[1])
    print(solve(n,k))