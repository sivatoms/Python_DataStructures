###############################
# Statck data structure.
# D
# C
# B
# A
###############################

class Stack:
    def __init__(self):
        self.items = []  # empty list
    
    def push(self, item):
        self.items.append(item)  # built in python function
    
    def pop(self):
        return self.items.pop()  #this will return top element in the stack beacause pop function always return pop item
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # -1 returns the last element in python

    def get_stack(self):
        return self.items

    def reverse_string(self, stack, input_string):
        
        # Loop through the string and push contents
        # character by character onto stack
        for i  in range(len(input_string)):
            stack.push(input_string[i])
        
        rev_str = ''
        while not stack.is_empty():
            rev_str += stack.pop()
        
        return rev_str

input_string = 'Hello'

s = Stack()

print(s.is_empty())
s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.is_empty())
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.peek())
print(s.reverse_string(s,input_string))