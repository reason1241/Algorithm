import sys

# brute force

shorts = sorted([int(sys.stdin.readline().strip()) for _ in range(9)])
total = sum(shorts)

result = []

for i in range(len(shorts)):
    for j in range(i, len(shorts)):
        if (total - shorts[i] - shorts[j]) == 100:
            for k in range(len(shorts)):
                if (k == i) or (k == j):
                    continue
                print(shorts[k])

            sys.exit(0)

sys.exit(1)