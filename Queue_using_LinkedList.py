# Implementing Queue using LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.rear = None

class Queue:
    def __init__(self):
        self.front = None
    
    def enqueue(self, val):
        if self.front is None:
            new_node = Node(val)
            self.front = new_node
            return
        new_node = Node(val)
        cur_node = self.front
        prev_node = None
        while cur_node:
            prev_node = cur_node
            cur_node = cur_node.rear
        
        prev_node.rear = new_node
        new_node.rear = None       
        
    def print_queue(self):
        cur_node = self.front
        while cur_node:
            print(cur_node.value, end=' ')
            cur_node = cur_node.rear
    
    def dequeue(self):
        pop_node = self.front
        next_node = self.front.rear
        self.front = next_node
        
        return pop_node.value
    

Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
Q.print_queue()
print('\nDequeued item is : ',Q.dequeue())
print('\nDequeued item is : ',Q.dequeue())
print('\nDequeued item is : ',Q.dequeue())
Q.print_queue()
