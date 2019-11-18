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
        
        cur_node = self.head
        prev_node = None
        if self.head is not None:
            while cur_node is not None:
                prev_node = cur_node
                cur_node = cur_node.previous
            
            prev_node.previous = new_node
            new_node.next = prev_node
            self.head = new_node

        else:
            self.head = new_node
            self.head.next = None
            self.head.previous = None
            
    
    def insert_at_end(self, val):
        new_node = Node(val)
        cur_node = self.head
        prev_node = None
        if self.head is not None:
            while cur_node is not None:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = new_node
            new_node.previous = prev_node
            
        else:
            self.head = new_node
            self.head.next = None
            self.head.previous = None
            return

    def traverse_list(self):
        if self.head is None:
            print('List is empty..')
        else:
            n = self.head           
            while n is not None:
                print(n.value, end = ' ')
                n = n.next

    #inserting a new node before a value
    def insert_a_node_at_value(self,new_elem,old_value):
        cur_node = self.head
        prev_node = None
        while cur_node and cur_node.value != old_value:
            prev_node = cur_node
            cur_node = cur_node.next
        
        new_node = Node(new_elem)
        new_node.next = cur_node
        new_node.previous = prev_node
        prev_node.next = new_node
        cur_node.previous = new_node


    # serach the node by value
    def search(self, val):
        if self.head is None:
            print('List is empty...')
            return
        
        cur_node = self.head
        counter = 0
        while cur_node:
            if cur_node.value == val:
                print('node found at : ', counter)
                return
            counter += 1
            cur_node = cur_node.next
    # delete the node by value
    def delete(self, val):
        if self.head is None:
            print("The list has no element to delete")
            return
        
        cur_node = self.head
        while cur_node:
            # when deleting head node of the list
            if self.head.value == val:
                temp = self.head.next
                self.head.next = None
                temp.previous = None
                self.head = temp
                return
            
            if cur_node.value == val:
                prev_node = cur_node.previous
                next_node = cur_node.next

                # when deleting last node of the list
                if next_node is None:
                    prev_node.next = None
                    return

                prev_node.next = next_node
                next_node.previous = prev_node
                return
            
            cur_node = cur_node.next
            

    # reverse the list
    def reverse_list(self):
        if self.head.previous is None and self.head.next is None:
            print('List has only one node : ', self.head.value)
            return
        temp = None
        n = self.head
       
        while n is not None:
            temp = n.previous
            n.previous = n.next
            n.next = temp
            n = n.previous
        
        if temp is not None:
            self.head = temp.previous
        
    
    # swap two nodes
    def swap_two_nodes(self, node1, node2):
        
        if node1 == node2:
            return
        
        cur_1 = self.head
        prev_1 = None
        while cur_1 and cur_1.value != node1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        cur_2 = self.head
        prev_2 = None
        while cur_2 and cur_2.value != node2:
            prev_2 = cur_2
            cur_2 = cur_2.next
        
        if prev_1:
            prev_1.next = cur_2
        else:
            cur_2.previous = None
            self.head = cur_2
        
        if prev_2:
            prev_2.next = cur_1
        else:
            cur_1.previous = None
            self.head = cur_1
        
        cur_1.next,cur_2.next = cur_2.next, cur_1.next
        cur_1.previous, cur_2.previous = cur_2.previous,cur_1.previous
        
n1 = DoubleLinkedList()
n1.make_list()
#n1.reverse_list()
n1.traverse_list()
#n1.insert_a_node_at_value(20,37)
print()
#n1.reverse_list()
#n1.delete(100)
#n1.search(37)
n1.swap_two_nodes(1,2)
n1.traverse_list()


