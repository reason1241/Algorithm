import sys

# brute force
# Time Complexity O(t * n^3) that n is the number of triangle numbers lower than 1000 324ms
# Space Complexity O(t + n) 30864kb
k = int(sys.stdin.readline().strip())

max_val = 0
inputs = []

for _ in range(k):
    cur_input = int(sys.stdin.readline().strip())
    max_val = max(cur_input, max_val)
    inputs.append(cur_input)
    
tri_nums = []
cur_base = 1
total = 0

while total < max_val:
    total += cur_base
    tri_nums.append(total)
    cur_base += 1
    
result = ""

for cur_input in inputs:
    success = False
       
    for t1_loc in range(len(tri_nums)):
        for t2_loc in range(t1_loc, len(tri_nums)):
            for t3_loc in range(t2_loc, len(tri_nums)):
                if tri_nums[t1_loc] + tri_nums[t2_loc] + tri_nums[t3_loc] == cur_input:
                    success = True
                    break
            if success:
                break
        if success:
            break
        
    if success:
        result += "1\n"
        continue
    result += "0\n"            
    
print(result)


#########
# brute force but with preprocessing
# Time Complexity O(t * n^3) that n is the number of triangle numbers lower than 1000 68ms
# Space Complexity O(t + n) 30864kb
import sys

k = int(sys.stdin.readline().strip())

max_val = 0
inputs = []

for _ in range(k):
    cur_input = int(sys.stdin.readline().strip())
    inputs.append(cur_input)
    
tri_nums = []
cur_base = 1
total = 0

while total <= 1000:
    total += cur_base
    tri_nums.append(total)
    cur_base += 1
    

two_tri = [False] * 1001

for i in range(len(tri_nums)):
    for j in range(i, len(tri_nums)):
        if tri_nums[i] + tri_nums[j] <= 1000:
            two_tri[tri_nums[i] + tri_nums[j]] = True
   
result = ""
         
for cur_in in inputs:
    success = False
    for tri_num in tri_nums:
        two_num = cur_in - tri_num
        if (0 < two_num <= 1000) and two_tri[two_num]:
            result +="1\n"
            success = True
            break
    if not success:
        result += "0\n"
            
print(result)