nums = [1,2,3,1,1,3]
#OP = 4

i = 0
j = i + 1
count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
            # lis.append(nums[i], nums[j])
            # print(lis)
            print(count)