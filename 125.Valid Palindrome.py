s = "A man, a plan, a canal: Panama"

print(len(s))

newStr = ""

for c in s:
    if c.isalnum():
        newStr += c.lower()
    print(newStr == newStr[::-1])




# print(len(s))

# newStr = ""

# for c in s:
#     if c.isalnum():
#         newStr += c.lower()
#     newStr == newStr[::-1]