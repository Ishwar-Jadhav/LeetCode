gain = [-4,-3,-2,-1,4,3,2]
#OP = 1
#OP = 0

currAltitude = 0
maxAltitude = 0

for i in gain:
    currAltitude += gain[i]
    maxAltitude= max(currAltitude,maxAltitude)








# prefix = 0
# altitude = []
# for i in range(len(gain)):
#     prefix += gain[i]
#     altitude.append(prefix)
# if max(altitude) <= -1:
#     altitude.append(0)
# print(altitude)
# print(max(altitude))