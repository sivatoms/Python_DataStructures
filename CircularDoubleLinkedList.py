# circular double linked lists has two pointer such as next, previous in circular form without having any null pointers

class Node:
    def __init__(self, value):
        self.value = value
        self.next = value
        self.previous = value

# creating circular double linked list
class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.start = None
    
    def make_list(self):
        nums = int(input('Enter size of the list : '))
        print('\n1. Insert at end \n2. Insert at start \n3. Insert at any index')
        pick = int(input('Choose any option : '))
        for _ in range(nums):
            val = input('Enter node : ')
            if pick == 1:
                self.insert_node_at_end(val)
            elif pick == 2:
                self.insert_node_at_first(val)
            else:
                pass
    
    def insert_node_at_end(self, val):
        new_node = Node(val)

        if self.head is not None:
            cur_node = self.head
            while cur_node:           
                if self.head == cur_node.next:
                    break
                cur_node = cur_node.next

            cur_node.next = new_node
            new_node.next = self.head
            new_node.previous = cur_node
            self.head.previous = new_node          
            
        else:
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
                        
        
    def insert_node_at_first(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.next = self.head
            new_node.previous = self.start
            self.head.previous = new_node
            self.start.next = new_node
            self.head = new_node
        else:
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            self.start = new_node
        

    def traverse_list(self):
        n = self.head
        if n is None:
            print('List is empty ..')
            return
        print('----------------------------')
        while True:
            print(n.previous.value, ' - ',n.value, ' - ', n.next.value)
            #print(n.value)
            if self.head == n.next:
                break
            n = n.next
            
    def search_node(self, val):
        if self.head is None:
            print('List is empty..')
            return
        n = self.head
        flag = False
        while True:
            if n.value == val:
                flag = True
                break
            n = n.next
        if flag:
            print('Found value')
        else:
            print('Not found')
    # delete any node from the list
    def delete_node(self, val):
        if self.head is None:
            print('List is empty..')
            return
        cur_node = self.head
        while cur_node:
            if cur_node.value == val:
                nxt = cur_node.next
                prev = cur_node.previous
                if cur_node == self.head:
                    nxt.previous = prev
                    prev.next = nxt
                    self.head = nxt
                else:
                    nxt.previous = prev
                    prev.next = nxt

            if self.head == cur_node.next:
                break
            cur_node = cur_node.next
    # swap two nodes
    def swap_two_nodes(self, node1, node2):
        cur_node_1 = self.head
        cur_node_2 = self.head

        while cur_node_1:
            if cur_node_1.value == node1:
                break
            if self.head == cur_node_1.next:
                break
            cur_node_1 = cur_node_1.next
        while cur_node_2:
            if cur_node_2.value == node2:
                break
            if self.head == cur_node_2.next:
                break
            cur_node_2 = cur_node_2.next
   
        # if the node2 is next of node1
        if cur_node_1.next == cur_node_2:
            prev_1 = cur_node_1.previous
            next_2 = cur_node_2.next

            prev_1.next = cur_node_2
            cur_node_2.previous = prev_1
            cur_node_2.next = cur_node_1
            
            next_2.previous = cur_node_1
            cur_node_1.next = next_2
            cur_node_1.previous = cur_node_2

            if self.head == cur_node_1:
                self.head = cur_node_2
                return
            if self.head == cur_node_2:
                self.head = cur_node_1
                return
        
        # if the node1 is next of node2
        elif cur_node_2.next == cur_node_1:
            prev_2 = cur_node_2.previous
            next_1 = cur_node_1.next

            prev_2.next = cur_node_1
            cur_node_1.previous = prev_2
            cur_node_1.next = cur_node_2
            
            next_1.previous = cur_node_2
            cur_node_2.next = next_1
            cur_node_2.previous = cur_node_1

            if self.head == cur_node_2:
                self.head = cur_node_1
                return
            if self.head == cur_node_1:
                self.head = cur_node_2
                return
        else:
            prev_1 = cur_node_1.previous
            next_1 = cur_node_1.next

            prev_2 = cur_node_2.previous
            next_2 = cur_node_2.next

            prev_1.next = cur_node_2
            cur_node_2.previous = prev_1
            cur_node_2.next = next_1
            next_1.previous = cur_node_2

            prev_2.next = cur_node_1
            cur_node_1.previous = prev_2
            cur_node_1.next = next_2
            next_2.previous = cur_node_1

            if self.head == cur_node_1:
                self.head = cur_node_2
                return
            if self.head == cur_node_2:
                self.head = cur_node_1
                return


    # reverse list
    def reverse_list(self):
        cur_node = self.head
        last_node = cur_node.previous
        while cur_node:
            nxt = cur_node.next

            prev_node = cur_node.previous
            next_node = cur_node.next

            cur_node.next = prev_node
            cur_node.previous = next_node

            if cur_node == last_node:
                temp = self.head
                self.head = last_node
                last_node.previous = temp
                temp.next = last_node

                break
            cur_node = nxt
    # checks if the list is palindrome or not
    def is_palindrome(self, n2):
        node_1 = self.head
        node_2 = n2.head
        flag = False

        while True:
            if node_1.value == node_2.value:
                flag = True
            else:
                flag = False
                break
            if self.head == node_1.next:
                break
            node_1 = node_1.next
            node_2 = node_2.next   
        return flag


if __name__ == '__main__':
    n1 = CircularDoubleLinkedList()
    n1.make_list()
    #print('--------------------------')
    n1.traverse_list()
    #n1.search_node(37)
    #n1.delete_node(37)
    #n1.swap_two_nodes(37,100)
    print('--------------------------')
    #n1.reverse_list()

    #import copy
    #n2 = copy.deepcopy(n1)
    #n2.reverse_list()
    #n2.traverse_list()
    #print(n1.is_palindrome(n2))
    
    n1.traverse_list()