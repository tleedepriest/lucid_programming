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
            # we have to check for last_node.next_node is not None
            # if we only check last_node, last_node will be set to None once
            # we exit loop, then we get an error.
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

            # don't raise error here like append because we kept track
            # of the previous node, which is guarantteed to exist once exit loop.
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

    def merge_sort(self, ll):
        """
        Example
        1 -> 3 -> 5 -> 7 -> 9
        2 -> 4 -> 6 -> 8 -> 10

        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
        """
        p = self.head
        q = ll.head
        # s points to lesser element and points to either p and q
        # trails p and q
        s = None
        if not p:
            return q

        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next_node
            else:
                s = q
                q = s.next_node

            new_head = s

        while p and q:
            if p.data <= q.data:
                # s.next is temporary value
                # s used to be p or q, so here we are changing the pointer
                # from previous p or q to the lessert value
                s.next_node = p
                # make sure it still tracks the lesser value
                s = p
                # move p up one
                p = s.next_node
            else:
                s.next_node = q
                s = q
                q = s.next_node

        if not p:
            s.next_node = q

        if not q:
            s.next_node = p

        return new_head

    def remove_duplicates(self):
        data = {}
        cur_node = self.head
        prev_node = None

        while cur_node:

            if cur_node.data not in data:
                data[cur_node.data] = cur_node
                prev_node = cur_node #update the previous node
            else:
                prev_node.next_node = cur_node.next_node
                cur_node = None #does this do anything??

            cur_node = prev_node.next_node

    def find_n_to_last(self, n_to_last):
        """
        returns the data element of the nth to last node.
        """
        length = self.get_length()

        # go through list again but now no where n_to_last is
        cur_node = self.head
        while length > n_to_last:
            cur_node = cur_node.next_node
            length-=1

        if cur_node is None:
            print(f"The value {n} is longer than the length of the list.")
        return cur_node.data

    def count_occurences(self, data):
        """
        counts the number of occurences of data in linked
        list
        """
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                count+=1
            cur_node = cur_node.next_node

        return count

    def count_occurences_rec(self, node, data):
        """
        recursive implementation of the program above.
        """
        if node is None:
            return 0
        else:
            if node.data == data:
                return 1 + self.count_occurences_rec(node.next_node, data)
            return self.count_occurences_rec(node.next_node, data)

    def rotate_list(self, rotate_data):
        """
        if rotate_data = 4, for given list
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
        rotating about point 4 gives
        5 -> 6 -> 1 -> 2 -> 3 -> 4 -> None
        """
        cur_node = self.head
        after_rotate = None
        rotate = None
        while cur_node.next_node:
            if cur_node.data == rotate_data:
                rotate = cur_node
                after_rotate = cur_node.next_node

            cur_node = cur_node.next_node
        # at last node after exiting while loop
        last_node = cur_node

        if rotate and after_rotate:
            rotate.next_node = None
            last_node.next_node = self.head
            self.head = after_rotate



if __name__ == "__main__":
    l = LinkedList()
    l.append("A")
    l.append("B")
    l.append("C")
    l.append("D")
    l.append("E")
    l.append("E")
    print(l.count_occurences("E"))
    print(l.count_occurences_rec(l.head, 'E'))
    print(l.count_occurences('G'))
    print("rotating list about point C")
    l.rotate_list('C')
    l.print_list()
    third_to_last = l.find_n_to_last(3)
    print(f"third to last {third_to_last}")
    l.print_list()
    print(l.swap_nodes('A', 'C'))
    l.print_list()
    l.reverse_iter()
    l.print_list()
    l.reverse_recursive()
    l.print_list()
    ll_one = LinkedList()
    ll_two = LinkedList()
    for i in [x for x in range(0, 10) if x%2==1]:
        ll_one.append(i)

    for i in [x for x in range(0, 10) if x%2==0]:
        ll_two.append(i)

    ll_one.print_list()
    ll_two.print_list()
    new_l = ll_one.merge_sort(ll_two)
    ll_one.print_list()
    new_l = LinkedList()
    for i in [0,0, 0, 0, 8, 9, 10]:
        new_l.append(i)
    new_l.print_list()
    new_l.remove_duplicates()
    new_l.print_list()
