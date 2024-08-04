candies = [2, 3, 5, 1, 3]
extra_candies = 3

n = []
for i in candies:
    n.append(i + extra_candies >= max(candies))
# return "n'
print(n)