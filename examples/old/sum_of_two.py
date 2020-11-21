import re

tgt = 0
nums = {}

exists = False

with open('input.txt', 'r') as inp:
    tgt = int(inp.readline().strip())
    num_iter = re.finditer('[0-9]+', inp.readline())

    for match in num_iter:
        num = int(match.group(0))

        if num > tgt:
            continue

        if not num in nums.keys():
            nums[num] = 1
        else:
            nums[num] += 1

        sub = tgt - num

        if sub in nums.keys() and (sub == num and nums[sub] > 1 or sub != num and nums[sub] >= 1):
            exists = True
            break

with open('output.txt', 'w') as out:
    out.write(str(1 if exists else 0)) 