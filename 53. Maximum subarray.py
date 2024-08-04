nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

maxSub = nums[0]
curSum = 0

for n in nums:
    print(n, end = " ")
    if curSum < 0:
        curSum = 0
    curSum += n
    print("Sum = ", curSum)
    maxSub = max(curSum, maxSub)

print("Ans = ", maxSub)