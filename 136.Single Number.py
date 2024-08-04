nums = [4,1,2,1,2]
# Output: 4
xor = 0

for i in range(len(nums)):
    xor ^= nums[i]

print(xor)