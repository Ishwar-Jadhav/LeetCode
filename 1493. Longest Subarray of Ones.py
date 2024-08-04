nums = [1, 1, 0, 1]

l = 0
zeros = 1

for r in range(len(nums)):
    if nums[r] == 0:
        zeros -= 1
    if zeros < 0:
        if nums[l] == 0:
            zeros += 1
        l += 1
print(r-l)
