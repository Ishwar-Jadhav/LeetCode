import LinkedList

head = [1 ,2 , 3, 4, 5]

if head.next == None:
    print(head)
curr = 0
while curr.next != None:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev


