class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        """
        print list from left to right
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def append(self, data):
        """
        append to end of list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        else:
            last_node = self.head
            while last_node.next_node:
                last_node = last_node.next_node
            last_node.next_node = new_node

    def get_length(self):
        curr_node = self.head
        length = 0
        
        while curr_node:
            curr_node = curr_node.next_node
            length+=1
        return length

    def get_length_recursive(self, node):
        
        if node is None:
            return 0
        return 1 + self.get_length_recursive(node.next_node)


    def prepend(self, data):
        """
        adds new data to beginning of list by redefining
        head and moving head
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """
        """
        # how does this condition work? need to modify somehow
        if not prev_node:
            print("previous node not in the list")
        else:
            new_node = Node(data)
            new_node.next_node = prev_node.next_node
            prev_node.next_node = new_node

    def delete_node(self, data):
        deleted_node = Node(data)
        # key to solving problem is declaring variable before
        # starting the loop
        cur_node = self.head
        if cur_node and curr == deleted_node:
            self.head = cur_node.next_node
            cur_node = None
        else:
            prev = None
            while cur_node and cur_node != deleted_node:
                prev = cur_node
                cur_node = cur_node.next_node
             
             # element in node not present
            if cur_node is None:
                return
            else:
                # pointer object of previous node set tobe deleted nodes next
                # node
                prev_node.next_node = cur_node.next_node
                cur_node = None

    def delete_node_by_position(self, index):
        """
        Deletes a node at 0 indexed index
        """
        position = 0
        curr_node = self.head
        if position == index:
            # move head to next node
            self.head = curr_node.next_node
            # delete head
            curr_node= None
        else:
            previous_node = None
            while position < index and curr_node:
                previous_node = curr_node
                curr_node = curr_node.next_node
                position+=1

            previous_node.next_node = curr_node.next_node
            curr_node = None
            


if __name__ == "__main__":
    l = LinkedList()
    print(l.get_length())
    l.append("A")
    print(l.get_length())
    l.append("B")
    l.append("c")
    l.append("D")
    l.append("E")
    l.prepend("0")
    l.insert_after_node(l.head.next_node, 2)
    l.print_list()
    l.delete_node_by_position(3)
    l.print_list()
    print(l.get_length())
    print(l.get_length_recursive(l.head))
