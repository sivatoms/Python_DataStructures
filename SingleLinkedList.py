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
  
n1 = SingleLinkedList()
n1.make_list()
#n1.insert_a_node_at_start(11)
#n1.insert_a_node_at_index(33,2)
n1.print_list()
#n1.delete_elem(72)
#n1.print_list()
print('')
n1.swap_nodes(1,3)
n1.print_list()



             
