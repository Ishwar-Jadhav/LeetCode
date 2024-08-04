asteroids = [-2,-2,1,-2]
#op = [5, 10]

stack = []
for a in asteroids:
    while stack and a < 0 < stack[-1]:
        if stack[-1] + a < 0:
            stack.pop()
        elif stack[-1] + a > 0:
            break
        else:
            stack.pop()
            break
    else:
        stack.append(a)
print(stack)



