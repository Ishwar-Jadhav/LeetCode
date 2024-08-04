nums = [2,2,1,1,1,2,2]
# Output: 3

nums.sort()
# print(nums)

l = 0
r = 1
count = 1

for i in range(len(nums)):
    if nums[l] == nums[r]:
        # print(nums[l])
        r += 1
        l += 1
        count += 1
        # print("count = ", count)
    maxCount = count
    if nums[l] != nums[r]:
        count = 0
        l += 1
        continue
print(max(maxCount, count))
    
