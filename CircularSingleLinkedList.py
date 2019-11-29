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
        print('Choose on of the option to insert :\n1.Insert at end\n2.Insert at start\n3.Insert at any node\nChoose : ', end='')
        pick = int(input())
        nums = int(input('Enter number of nodes you want to insert : '))
        for _ in range(nums):
            val = int(input('Enter node value : '))
            if pick == 1:
                self.insert_node_at_end(val)
            elif pick == 2:
                self.insert_at_start(val)
            elif pick == 3:
                self.insert_at_any_node(val,old_elem=None)
            else:
                return
        print('-----------------------------------')
    #prepend
    def insert_at_start(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.next = self.head
            self.start.next = new_node
            self.head = new_node
        else:
            new_node.next = new_node
            self.head = new_node
            self.start = new_node

    # append
    def insert_node_at_end(self,val):
        new_node = Node(val)
        if self.head is not None:
            cur_node = self.head
            while cur_node:           
                if self.head == cur_node.next:
                    break
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

        else:
            self.head = new_node
            new_node.next = new_node
            
    # insert at any node before the value
    def insert_at_any_node(self, new_elem, old_elem):
        cur_node = self.head
        prev_node = None
        while cur_node and cur_node.value != old_elem:
            prev_node = cur_node
            if self.start == cur_node.next:
                break
            cur_node = cur_node.next
        
        new_node = Node(new_elem)
        new_node.next = cur_node
        prev_node.next = new_node
        if new_node.value == self.start:
            self.head = new_node
            self.start = new_node

    
    def traverse_list(self):
        if self.head is None:
            print('List is empty..')
            return
        cur_node = self.head
        while True:
            print('The node value : ',cur_node.value, cur_node.next.value) 
            cur_node = cur_node.next           
            if self.head == cur_node:
                break            
      
    # delete or remove any value
    def remove_by_value(self, val):
        if self.head is None:
            print('List is empty..')
            return
        if self.head.value == val:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.value == val:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next
    # delete or remove any node
    def remove_by_node(self, node):
        if self.head is None:
            print('List is empty..')
            return
        if self.head == node:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node == node:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next


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
    
    # swap two nodes 
    def swap_two_nodes(self, node1, node2):
        if node1 == node2:
            return
        
        cur_1 = self.head
        prev_1 = None
        while cur_1 and cur_1.value != node1:
            prev_1 = cur_1
            cur_1 = cur_1.next
            if self.start == cur_1.next:
                break
        
        cur_2 = self.head
        prev_2 = None
        while cur_2 and cur_2.value != node2:
            prev_2 = cur_2
            cur_2 = cur_2.next
            if self.start == cur_2:
                break
        
        if (cur_1.value != node1 or cur_2.value != node2):
            return
        # if prev_1 node is none (it means the node1 is a head node) then we have to find the last node which points to head node
        if not prev_1:
            temp_1 = self.head
            while temp_1:
                if temp_1.next == self.head:
                    break
                temp_1 = temp_1.next
            prev_1 = temp_1
            self.head = cur_2
            self.start = cur_2
        # if prev_2 node is none (it means the node2 is a head node) then we have to find the last node which points to head node
        if not prev_2:
            temp_2 = self.head
            while temp_2:
                if temp_2.next == self.head:
                    break
                temp_2 = temp_2.next
            prev_2 = temp_2
            self.head = cur_1
            self.start = cur_1
        
        prev_1.next, prev_2.next = cur_2, cur_1
        cur_1.next, cur_2.next = cur_2.next, cur_1.next            

    # length of circular linkd list
    def __len__(self):
        cur_node = self.head
        counter = 0
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return counter


    # josephus problem is remove nodes in josephus step size position from each of it's nodes utill it hits node less than josephus step size
    def josephus_problem(self, step):
        cur_node = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur_node = cur_node.next
                count += 1
            self.remove_by_node(cur_node)
            cur_node = cur_node.next



if __name__=='__main__':
    n1 = CircularSingleLinkedList()
    n1.make_list()
    #print('------------------')
    #n1.traverse_list()
    #n1.delete_node(37)
    #n1.search_node(100)
    #n1.insert_at_any_node(99,37)
    #n1.delete_node(12)
    #n1.swap_two_nodes(12,22)
    n1.traverse_list()
    print(len(n1))
    print('-----------------------')
    n1.josephus_problem(2)
    n1.traverse_list()