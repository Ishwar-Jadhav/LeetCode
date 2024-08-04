'''
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]
'''


def __init__(self, size: int):
    self.size = size
    self.queue = []


def next(self, val: int) -> float:
    size, queue = self.size, self.queue
    queue.append(val)

    windowSum = sum(queue[-size:])

    return windowSum / min(len(queue), size)
