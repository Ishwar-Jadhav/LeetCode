nums = [0,3,7,2,5,8,4,6,0,1]
#OP = 4 (1, 2, 3, 4)

if not nums:
    print(0)

nums.sort()

current_streak = 1
longest_streak = 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        if nums[i] == nums[i - 1] + 1:
            current_streak += 1
        else:
            longest_streak = max(current_streak, longest_streak)
            current_streak = 1
print(max(longest_streak, current_streak))
