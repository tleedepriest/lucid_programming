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

    def swap_nodes(self, swap_one, swap_two):
        """
        swap two nodes in linked list.
        two cases, either netiher node is at tthe head
        or at least one node is at the head.
        """
        if swap_one == swap_two:
            return

        curr_node_one = self.head
        previous_node_one = None

        while curr_node_one and curr_node_one.data != swap_one:
            previous_node_one = curr_node_one
            curr_node_one = curr_node_one.next_node

        curr_node_two = self.head 
        previous_node_two = None
        while curr_node_two and curr_node_two.data != swap_two:
            previous_node_two = curr_node_two
            curr_node_two = curr_node_two.next_node

        # if these values don't exist, stop
        if not curr_node_one or not curr_node_two:
            return

        if previous_node_one:
            previous_node_one.next_node = curr_node_two
        else:
            self.head = curr_node_two

        if previous_node_two:
            previous_node_two.next_node = curr_node_one
        else:
            self.head = curr_node_one

        (curr_node_one.next_node, 
         curr_node_two.next_node) = (curr_node_two.next_node, 
                                     curr_node_one.next_node)


    def reverse_iter(self):
        """
        A -> B -> C -> D -> None
        just flip the arrows
        A <- B < - C <- D < - None
        """
        prev = None
        curr = self.head
        
        while curr:
            nxt = curr.next_node # temp variable
            curr.next_node = prev
            prev = curr
            curr = nxt

        self.head = prev

    def reverse_recursive(self):
        
        def _reverse_recursive(curr, prev):
            """

            """
            if not curr:
                return prev

            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)

if __name__ == "__main__":
    l = LinkedList()
    l.append("A")
    l.append("B")
    l.append("C")
    l.append("D")
    l.append("E")
    l.print_list()
    print(l.swap_nodes('A', 'C'))
    l.print_list()
    l.reverse_iter()
    l.print_list()
    l.reverse_recursive()
    l.print_list()
