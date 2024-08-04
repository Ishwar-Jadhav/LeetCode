nums = [2,3,1,1,4]

goal = len(nums) - 1

for i in range(len(nums) - 1, -1, -1):
    print("i = ", i)
    if i + nums[i] >= goal:
        print("sum = ", i + nums[i])
        goal = i
        # print(goal)
