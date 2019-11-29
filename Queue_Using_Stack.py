# Queue is an Abract Data structure
# It follows a particular particular order in which operations are performed
# The order is First In First Out (FIFO)
# the difference between a Stack and Queue is in removing. In stack we remove the item the most recently added, in Queue, we remove the item at first

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # Method 1 using two stacks to implement the enquee
    def enqueue(self,val):        
        # here the stack 1 pushes items to stack2
        while self.IsEmpty(self.stack1):
            self.stack2.append(self.stack1.pop())

        self.stack1.append(val)

        # here stack2 pushes back all items to stack2 qhich will form a queue
        while self.IsEmpty(self.stack2):
            self.stack1.append(self.stack2.pop())

    def push(self):               
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        return self.stack1.pop()
    
    def IsEmpty(self,stack):
        if stack == []:
            return False
        return True

    def peek(self):
        return self.stack1[-1]

    def print_queue(self):
        return self.stack1

if __name__ == '__main__':
    Q = Queue()
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)
    Q.enqueue(40)
    Q.enqueue(50)
    print(Q.print_queue())
    print('Peek item : ', Q.peek())
    print(Q.dequeue())
    print(Q.print_queue())