nums = [9,6,4,2,3,5,7,0,1]
# Output: 8    


n = len(nums)
flag = 0

for i in range(1, n + 1):
    print("i = ", i)
    flag = flag ^ i
    print("flag1 = " , flag)

for num in nums:
    print("num = ", num)
    flag = flag ^ num
    print("flag2 = ", flag)

print("Missing number = ", flag)