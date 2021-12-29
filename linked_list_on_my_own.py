class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def append(self, data):
        """
        need to go through linked list to append
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            # wont enter loop if only a single node...
            while last_node.next_node:
                last_node = last_node.next_node

            last_node.next_node = new_node

l = LinkedList()
l.append("A")
l.append("B")
print(l)
l.print_list()
