import sys

# brute force
k = int(sys.stdin.readline().strip())

max_val = 0
inputs = []

for _ in range(k):
    cur_input = int(sys.stdin.readline().strip())
    max_val = max(cur_input, max_val)
    inputs.append(cur_input)