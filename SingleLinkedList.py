# Static class Node which creates a new node each time a new node entered
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# creating single linked list class to create dynamic node list
class SingleLinkedList:
    def __init__(self):
        self.head = None  # initially we aasign None as headnode
    
    #function to create a node list
    def make_list(self):
        print('Pick type of insertion you want to do :  1.Insert at start  2. Insert at end  3. Insert at any index \n Choose one of the option : ', end='')
        pick = int(input())
        nums = int(input('Enter the length of the node : '))
        print('Enter node values : ', end=' ')
        while nums > 0:
            elem = int(input())
            if pick == 1:
                self.insert_a_node_at_start(elem)
            elif pick == 2:
                self.insert_a_node_at_end(elem)
            elif pick == 3:
                index = int(input('Enter index : '))
                self.insert_a_node_at_index(elem, index)
            else:
                pass
            nums -= 1
    
    # create a function to insert new element at end each time when it is called
    def insert_a_node_at_end(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_a_node_at_start(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node    
    
    # insert elem at any index after an elem
    def insert_a_node_at_index(self,elem,position):
        counter = 0
        n = self.head
        while n is not None:
            if counter == position:
                new_node = Node(elem)
                new_node.next = n.next
                n.next = new_node
                break
            counter += 1
            n = n.next

    # create a function to view the entire list
    def print_list(self):
        if self.head is None:
            print('The list is empty')
        else:
            curr = self.head
            print('The entire node elements are : ', end=' ')
            while curr:
                print(curr.value, end=' ')
                curr = curr.next

    # size of the list using iterative process
    def size_of_node(self):
        if self.head is None:
            print('List is empty..')
        else:
            n = self.head
            counter = 0
            while n is not None:
                counter += 1
                n = n.next
        return counter
    
    # search an element in the node
    def search_elem(self, elem):
        if self.head is None:
            print('List is empty..')
        else:
            n = self.head
            while n is not None:
                if n.value == elem:
                    flag = True
                    break
                else:
                    flag = False
                n = n.next
            if flag:
                print('\nFound the element in the list')
            else:
                print('\nNot found the element in the list')

    # delete en element from the list in between first and last
    def delete_elem(self, elem):
        if self.head is None:
            print('List is empty..')
        else:
            curr = self.head
            if curr.value == elem:
                self.head = curr.next
                curr = None
                return
            else:
                while curr is not None:
                    if curr.next.value == elem and curr.next is not None:
                        curr.next = curr.next.next
                        break
                    elif curr.next is None:
                        pass
                    curr = curr.next
    
    # swap two nodes
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.value != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.value != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1  
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    # reverse list using iteratively
    def reverse_list_iterative(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev

            self.print_helper(prev, 'PREV')
            self.print_helper(cur_node, 'CUR')
            self.print_helper(nxt, 'NXT')
            print('\n')

            prev = cur_node
            cur_node = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur_node,prev):
            if not cur_node:
                return prev
            
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt

            return _reverse_recursive(cur_node, prev)
        
        self.head = _reverse_recursive(cur_node=self.head, prev=None)

    # print helper for reverse a string
    def print_helper(self, node, name):
        if node is None:
            print(name + ': None')
        else:
            print(name + ':' , node.value)


    # purely using two sorted linked lists 
    def merge_sorted(self, n2):
        p = self.head
        q = n2.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p.value <= q.value:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        new_head = s

        while p and q:
            if p.value <= q.value:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q

        if not q:
            s.next = p
        
        return new_head

    # remove duplicates from the list
    def remove_duplicates(self):
        cur_node = self.head
        prev_node = None
        dup_dict = dict()
        while cur_node:
            if cur_node.value in dup_dict:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                # have not encountered element before
                dup_dict[cur_node.value] = 1
                prev_node = cur_node
            cur_node = prev_node.next

    # finding the nth from last node means - have to find the node element from last node till nth position
    def print_nth_from_last(self, n):
        # Method 1
        '''
        lngth = self.size_of_node()
        cur_node = self.head
        while lngth > 0:
            if lngth == n:
                print('The nth node from the last is : ', cur_node.value)
                return cur_node

            cur_node = cur_node.next
            lngth -= 1
        
        if cur_node is None:
            return
        '''
        # Method 2
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        
        if not q:
            print(str(n) + ' n is greater than number of nodes in list')
        
        while p and q:
            p = p.next
            q = q.next
        
        return p.value

    # count number of occurences of any node in the list
    # iterative approach
    def count_occurences_iterative(self, data):
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.value == data:
                count += 1        
            cur_node = cur_node.next
        
        return count
    
    # recursive approach to count number of occurences of a node
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        
        if node.value == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    # rotate elements after nth node
    def rotate_nth_node(self, data):
        cur_node = self.head
        last_node = None
        while cur_node:            
            if cur_node.value == data:
                last_node = cur_node.next
                cur_node.next = None
                break
            cur_node = cur_node.next
        temp = self.head
        while last_node:           
            nxt = last_node.next
            last_node.next = temp
            temp = last_node
            self.head = last_node
            last_node = nxt


n1 = SingleLinkedList()
n1.make_list()
#n2 = SingleLinkedList()   used for sorting of two sorted linked lists
#n2.make_list()
#n1.merge_sorted(n2)
#n1.print_list()
#n1.insert_a_node_at_start(11)
#n1.insert_a_node_at_index(33,2)
#n1.print_list()
#n1.delete_elem(72)
#n1.print_list()
#print('')
#n1.swap_nodes(1,3)
#n1.reverse_list_iterative()
#n1.reverse_recursive()
#n1.remove_duplicates()
#print(n1.print_nth_from_last(2))
n1.print_list()
#print('\n',n1.count_occurences_iterative(1))
#print('\n',n1.count_occurences_recursive(n1.head, 1))
n1.rotate_nth_node(2)
n1.print_list()



             
