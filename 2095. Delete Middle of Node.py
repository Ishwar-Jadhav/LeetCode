from LinkedList import LinkedList

# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.
head = [1,3,4,7,1,2,6]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.n = 0

    if head.next == None:
        print(None)

    count = 0
    p1 = p2 = head

    while p2 != None:
        p1 = p1.next
        count += 1
    mid == count // 2
    print(mid)

    for i in range(mid):
        p2 = p2.next


'''
if head == None:
            return None
        
        count = 0
        p1 = p2 = head

        while p2 != None:
            count += 1
        mid = count // 2
        print(mid)

        for i in range(mid - 1):
            p2 = p2.next
        p2.next = p2.next.next

        return head 
'''