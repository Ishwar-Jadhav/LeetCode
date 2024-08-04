'''
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
'''

s = "(1+(2*3)+((8)/4))+1"
print(s)

stack, res = [], 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
        res = max(res, len(stack))
    elif s[i] == ")":
        stack.pop()
print(stack)
print(res)