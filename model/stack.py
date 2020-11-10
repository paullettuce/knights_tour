from collections import deque


class Stack:

    def __init__(self, max_size):
        self.items = deque(maxlen=max_size)
        self.max_size = max_size

    def top(self):
        return self.items.__getitem__(self.size()-1)

    def size(self):
        return self.items.__len__()

    def empty(self):
        return self.size() == 0

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def get(self, i):
        return self.items.__getitem__(i)

    def __contains__(self, o):
        return o in self.items

    def as_list(self):
        return list(self.items)

    def reverse(self):
        self.items.reverse()

    def is_full(self):
        return self.size() == self.max_size
