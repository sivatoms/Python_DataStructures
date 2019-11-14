# Double Linked Lists
# It has one next node reference, one previous node reference which allows the lists to traverse in both directions

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# creating Double Linked Lists class to create a new list and adding insert, search, delete functions to it.

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    

    def make_list(self):
        pick = int(input('pick a type of insert you want to do\n  1 . Insert at the front \n  2 . Insert at the end \n  3 . Insert at any given node \n Choose : '))
        nums = int(input('Enter the nummber of nodes you want to enter : '))
        for _ in range(nums):
            val = int(input('enter node values : '))
            if pick == 1:
                self.insert_at_start(val)
            elif pick == 2:
                self.insert_at_end(val)
            elif pick == 3:
                pass
    

    def insert_at_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        new_node.previous = None
        if self.head is not None:
            self.head.previous = new_node
        self.head = new_node
    
    def insert_at_end(self, val):
        new_node = Node(val)
        new_node.next = None
        new_node.previous = self.head
        if self.head is not None:
            self.head.next = new_node
        self.head = new_node

    def traverse_list_from_start(self):
        if self.head is None:
            print('List is empty..')
        else:
            n = self.head
            print('All nodes are : ', end=' ')
            if n.next is None:
                while n is not None:
                    print(n.value, end = ' ')
                    n = n.previous
            else:
                while n is not None:
                    print(n.value, end = ' ')
                    n = n.next

    def traverse_list_from_end(self):
        if self.head is None:
            print('List is empty..')
        else:
            n = self.head
            print('All nodes are : ', end=' ')
            if n.next is None:
                while n is not None:
                    print(n.value, end = ' ')
                    n = n.previous
            else:
                while n is not None:
                    print(n.value, end = ' ')
                    n = n.next
    # serach the node by value
    def search(self, val):
        if self.head is None:
            print('List is empty...')
        else:
            n = self.head
            if n.next is None:
                while n is not None:
                    if n.value == val:
                        print('\nFound the value')
                        break
                    n = n.previous
            else:
                while n is not None:
                    if n.value == val:
                        print('\nFound the value')
                        break
                    n = n.next
    
    # delete the node by value
    def delete(self, val):
        if self.head is None:
            print("The list has no element to delete")
            return

        # this is for the insert_at_start list where self.head.previous is always None
        if self.head.previous is None:
            # if the node is at the start position of the list
            if self.head.value == val:
                n = self.head.next
                self.head = n
                self.head.previous = None
                return
            else:
                n = self.head
                while n.next is not None:
                    if n.value == val:
                        break
                    n = n.next
                # if the node is at last position of the list
                if n.next is None:
                    temp = n.previous
                    self.head = temp
                    self.head.next = None
                    return
                else:
                # if node is in the middle of the list
                    temp_next = n.next
                    temp_prev = n.previous
                    temp_next.previous = n.previous
                    temp_prev.next = n.next
                    return

        # this is for the insert_at_end list where self.head.next is always None
        if self.head.next is None:
            # if node is at last position o the list 
            if self.head.value == val:
                n = self.head.previous
                self.head = n
                self.head.next = None
                return
            else:
                n = self.head
                while n.previous is not None:
                    if n.value == val:
                        break
                    n = n.previous
                # if the node is at the start of the list
                if n.previous is None:
                    temp = n.next
                    self.head = temp
                    self.head.previous = None
                    return
                else:
                    # if the node is in the middle of the list
                    temp_next = n.next
                    temp_prev = n.previous
                    temp_next.previous = n.previous
                    temp_prev.next = n.next
                    return
        
    # reverse the list
    def reverse_list(self):
        


        
n1 = DoubleLinkedList()
n1.make_list()
#n1.traverse_list_from_start()
#n1.search(37)
#n1.delete(12)
#n1.traverse_list_from_start()
n1.reverse_list()