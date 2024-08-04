import queue
# numbers = [10, 20, 30, 40, 50, 60, 70]
# q = queue.LifoQueue()
# for number in numbers:
#     q.put(number)
#     # print(q.get())
# print(q.get())
# print(q.get())

# q = queue.PriorityQueue()
# q.put((2, "Hello World"))
# q.put((77, 77))
# q.put((23, True))
# q.put((1, 9))
#
# while not q.empty():
#     print(q.get())


# from collections import deque
#
# q = deque()
# q.append('a')
# q.append('b')
# q.append('c')
# print("Initial queue")
# print(q)
# print("\nElements dequeued from the queue")
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
#
# print("\nQueue after removing elements")
# print(q)



from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')

print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())