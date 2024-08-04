# n = int(input("Enter a number "))
# for i in range(n):
#     for j in range(i-1):
#         print("* " * n)

n = int(input("Enter the number "))
for i in range(1, n+1, 2):
    for j in range(i+1):
        print(j, end=" ")
    print("")
