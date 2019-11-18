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
        for _ in range(nums):
            val = int(input('Enter node : '))
            self.insert_node(val)
    
    def insert_node(self, val):
        new_node = Node(val)
        temp = self.head
        new_node.previous = None
        new_node.next = self.head

        if self.head is not None:            
            temp = self.start
            temp.previous = new_node
            new_node.previous = temp
            #new_node.next = self.head
                  
            #temp.next = new_node
            #temp.previous = new_node
        else:
            new_node.next = new_node
            new_node.previous = new_node
            self.start = new_node

        self.head = new_node
    
    def traverse_list(self):
        n = self.head
        if n is None:
            print('List is empty ..')
            return
        
        while True:
            print(n.previous.value ,n.value, n.next.value)
            if self.start.value == n.value:
                break
            n = n.next
           

if __name__ == '__main__':
    n1 = CircularDoubleLinkedList()
    n1.make_list()
    n1.traverse_list()