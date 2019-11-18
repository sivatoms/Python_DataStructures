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
        print('\n1. Insert at start \n2. Insert at end \n3. Insert at any index')
        pick = int(input('Choose any option : '))
        for _ in range(nums):
            val = int(input('Enter node : '))
            if pick == 1:
                self.insert_node_at_first(val)
            elif pick == 2:
                self.insert_node_at_end(val)
            else:
                pass
    
    def insert_node_at_first(self, val):
        new_node = Node(val)
        new_node.next = None
        
        if self.head is not None:
            new_node.next = self.head.next
            new_node.previous = self.head.previous
            self.head.previous = new_node

            temp = self.start
            temp.next = new_node
            print(new_node.previous.value, new_node.value, new_node.next.value)            
        else:
            new_node.next = new_node
            new_node.previous = new_node
            self.start = new_node
            print(new_node.previous.value, new_node.value, new_node.next.value)
        self.head = new_node
    
    def insert_node_at_end(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.previous = self.head
            new_node.next = self.head.previous
            self.head.previous = new_node

            temp = self.start
            temp.next = new_node
            temp.previous = self.head.next
            print(new_node.previous.value, new_node.value, new_node.next.value)     
        else:
            new_node.next = new_node
            new_node.previous = new_node
            self.start = new_node
            print(new_node.previous.value, new_node.value, new_node.next.value)
        self.head = new_node

    def traverse_list(self):
        n = self.head
        if n is None:
            print('List is empty ..')
            return
        print(n.previous.value,n.value, n.next.value)
        print(self.start.previous.value,self.start.value, self.start.next.value)
        print('----------------------------')
        k = 0
        while True:
            print(n.previous.value ,n.value, n.next.value)
            if self.start.value == n.value:
                break
            n = n.next
            if k == 6:
                
                break
            k += 1
    
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
    
    def delete_node(self, val):
        if self.head is None:
            print('List is empty..')
            return
        n = self.head
        while True:
            if n.value == val:
                temp_next = n.next
                temp_prev = n.previous
                temp_next.previous = n.previous
                temp_prev.next = n.next
                if self.start.value == val:  # if the start node is that you are deleting then the start node should be set to it's next node to stop the travsersing while traversing.
                    self.start = temp_next.next.next
                break
            n = n.next
        


if __name__ == '__main__':
    n1 = CircularDoubleLinkedList()
    n1.make_list()
    print('--------------------------')
    #n1.traverse_list()
    #n1.search_node(37)
    #n1.delete_node(37)
    n1.traverse_list()