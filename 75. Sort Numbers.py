nums = [2, 0, 2, 1, 1, 0]
#OP = [0, 0, 1, 1, 2, 2]

count0 = 0
count1 = 0
count2 = 0

for num in nums:
    if num == 0:
        count0 += 1
    elif num == 1:
        count1 += 1
    else:
        count2 += 1

for i in range(count0):
    nums[i] = 0
for i in range(count0, count0 + count1):
    nums[i] = 1
for i in range(count0 + count1, len(nums)):
    nums[i] = 2 