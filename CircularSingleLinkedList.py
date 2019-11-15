# circular linked list can be implemneted with single linked list,
# double linked list. the first node previous pointer is the last node next pointer. there are no nulls or None will be assigned to the pointers

class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.value


# Circular Single Linked List
class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.start = None  # this variable is to make a circular connection and it stores the first entered node
    
    def make_list(self):
        nums = int(input('Enter number of nodes you want to insert : '))
        for _ in range(nums):
            val = int(input('Enter node value : '))
            self.insert_node(val)
        print('-----------------------------------')

    def insert_node(self,val):
        new_node = Node(val)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            temp = self.start # this will always keep temp value as start node
            temp.next = new_node  # this will set the last node next to start
        else:
            # if the list is empty
            new_node.next = new_node
            self.start = new_node

        self.head = new_node
       
    
    def traverse_list(self):
        n = self.head
        if n is None:
            print('List is empty..')
            return

        while True:
            print('The node value : ',n.next.value, n.value)            
            if self.start.value == n.value:
                break
            n = n.next
    
    def delete_node(self, val):
        n = self.head
        if n is None:
            print('List is empty ..')
            return
        while True:
            if n.next.value == val:
                n.next = n.next.next
                break
            n = n.next
    def search_node(self, val):
        n = self.head
        if n is None:
            print('List is empty..')
            return
        if self.start.value == val:
            print('Found the value')
            return
        else:
            flag = False
            while True:
                if n.value == val:
                    flag = True
                    break
                n = n.next
            if flag:
                print('Found the value...')
            else:
                print('Not found the value...')


if __name__=='__main__':
    n1 = CircularSingleLinkedList()
    n1.make_list()
    #print('------------------')
    #n1.traverse_list()
    #n1.delete_node(37)
    print('------------------')
    n1.traverse_list()
    n1.search_node(100)