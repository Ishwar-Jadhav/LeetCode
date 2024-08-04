s = "lee(t(c)o)de)"
print(s)
stack = []
for i in range(len(s)):
    if s[i] == "(" or ")":
        stack.append(s[i])
    else:
        print("Fail")
    print(stack)