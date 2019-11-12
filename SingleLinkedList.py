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
        nums = int(input('Enter the length of the node : '))
        print('Enter node values : ', end=' ')
        while nums > 0:
            elem = int(input())
            self.insert_from_start(elem)
            nums -= 1
    
    # create a function to insert new element at begining each time when it is called
    def insert_from_start(self, elem):
        new_node = Node(elem)
        new_node.next = self.head
        self.head = new_node

    # create a function to view the entire list
    def print_list(self):
        if self.head is None:
            print('The list is empty')
        else:
            n = self.head
            print('The entire node elements forward direction (Left to Right) are : ')
            while n is not None:
                print(n.value, end=' ')
                n = n.next

    # size of the list
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
            n = self.head
            if n.value == elem:
                self.head = n.next
            else:
                while n is not None:
                    if n.next.value == elem:
                        n.next = n.next.next
                        print('Came here')
                        self.print_list()
                        break
                    n = n.next
n1 = SingleLinkedList()
n1.make_list()
#n1.print_list()
n1.delete_elem(37)
n1.search_elem(37)
n1.print_list()


             
