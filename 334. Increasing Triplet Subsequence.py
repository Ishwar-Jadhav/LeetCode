nums = [2, 1, 5, 0, 4, 6]

n1, n2 = float("inf"), float("inf")

for n in nums:
    if n < n1:
        n1 = n
    elif n < n2:
        n2 = n
    else:
        print("true")# return true
print("False")# return false