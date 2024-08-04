nums = [1,0,1,1,0,1]
#OP = 3

currCount = 0
maxCount = 0

for i in range(len(nums)):
    if nums[i] == 1:
        currCount += 1
        if maxCount < currCount:
            maxCount = currCount
        i += 1
    else:
        currCount = 0
        i += 1
    maxCount = max(maxCount, currCount)

print(maxCount)