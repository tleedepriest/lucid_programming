"""
https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1] #top of stack
    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(6)
    s.push('A')
    print(s.get_stack())
    print(s.peek())
