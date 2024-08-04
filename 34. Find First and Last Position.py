nums = [5,7,7,8,8,8,10]
target = 6
# Output: [3,4]

first, last = -1, -1

for i in range(len(nums)):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
print([first, last])



