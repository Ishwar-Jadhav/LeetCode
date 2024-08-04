nums = [0, 1, 0, 3, 12]

l = 0

for r in range(len(nums)):
    if nums[r]:
        print("r = ", r)
        print("l = ", l)
        print("rnum = ", nums[r], end=" \n")
        print("lnum = ", nums[l], end ="\n")
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
print(nums)
