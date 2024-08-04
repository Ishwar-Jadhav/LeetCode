# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
nums = [3,4,5,1,2]

cnt = 0
for i in range(len(nums)):
    print(i-1)
    if nums[i-1] > nums[i]:
        cnt += 1
print(cnt <= 1)