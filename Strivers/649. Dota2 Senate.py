from collections import deque
senate = "RDDRD "

senate = list(senate)

D, R = deque(), deque()

for i, c in enumerate(senate):
    if c == "R":
        R.append(i)
        print("R of i = ", i)
    else:
        D.append(i)
        print("D of i = ", i)

while D and R:
    dTurn = D.popleft()
    print("dTurn = ", dTurn)
    rTurn = R.popleft()
    print("rTurn = ", rTurn)

    if rTurn < dTurn:
        R.append(dTurn + len(senate))
        print("R = ", R)
    else:
        D.append(rTurn + len(senate))
        print("D = ", D)
print("R") if R else print("D")

