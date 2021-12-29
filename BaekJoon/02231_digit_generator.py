import sys
import math

# brute force
target = int(sys.stdin.readline().strip())
base = target - (int(math.log(target)) * 9)

for candidate in range(base, target):
    i = candidate
    digit_sum = i
    while i > 0:
        digit_sum += i % 10
        i = i // 10

    if digit_sum == target:
        print(candidate)
        sys.exit(0)

print(0)
sys.exit(0)

# import sys

# # brute force
# target = int(sys.stdin.readline().strip())

# for candidate in range(target - (9 * 7), target):
#     i = candidate
#     digit_sum = i
#     while i > 0:
#         digit_sum += i % 10
#         i = i // 10

#     if digit_sum == target:
#         print(candidate)
#         sys.exit(0)

# print(0)
# sys.exit(0)