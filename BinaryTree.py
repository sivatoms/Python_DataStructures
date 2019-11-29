# Binary Tree is a node may or may not have two child nodes in such way that the left chil node always less than the root and right child node always greater than root node
#
#             10
#         /       \
#        8         20
#      /   \     /    \
#     2     9  15      30
#####################################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
# Binary Tree class

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # mkae a tree
    def make_tree(self):
        nums = int(input('Enter number of nodes you want to insert : '))
        print('Pick any process below to insert\n1.InsertRecursive\n2.InsertIterative\nChoose option : ', end='')
        pick = int(input())
        for _ in range(nums):
            if pick == 1:
                self.insert_recursive(self.root,Node(int(input())))
            elif pick == 2:
                self.insert_iterative(Node(int(input())))
            else:
                print(str(pick) + ' is a wrong approach for insertion')
            

    # insert into binary tree using recursive approach
    def insert_recursive(self,root,new_node):
        if root is None:
            self.root = new_node
            root = self.root
        else:
            if root.value < new_node.value:
                if root.right is None:
                    root.right = new_node
                else:
                    self.insert_recursive(root.right, new_node)
            else:
                if root.left is None:
                    root.left = new_node
                else:
                    self.insert_recursive(root.left, new_node)

    # insert into binary tree using iterative approach
    def insert_iterative(self,new_node):
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            last_node = None
            # this loop will keep track of last node
            while cur_node is not None:
                last_node = cur_node
                # this condition will iterate for left node  
                if new_node.value < cur_node.value:
                    cur_node = cur_node.left
                else:
                # this condition will iterate for right node
                    cur_node = cur_node.right

            if new_node.value < last_node.value:
                # if the new node is less than root node then left child
                last_node.left = new_node
            else:
                # if the new node is greater than root node then right child
                last_node.right = new_node
                                       


    # print list
    def print_list(self):
        print('\nPick type of traversal you want see : \n\n1.Pre-Order-Recursive\n\n2.In-Order-Recursive\n\n3.Post-Order-Recursive\n\n4.Pre-Order-Iterative\n\n5.In-Order-Iterative\n\n6.Post-Order-Iterative\n\nChoose an option : ', end='')
        pick = int(input())
        if pick == 1:
            print('\n',self.print_pre_order(self.root,''),'\n')
        elif pick == 2:
            print('\n',self.print_in_order(self.root,''),'\n')
        elif pick == 3:
            print('\n',self.print_post_order(self.root,''),'\n')
        elif pick == 4:
            print('\n',self.pre_order_iter(),'\n')
        elif pick == 5:
            print('\n',self.in_order_iter(),'\n')
        elif pick == 6:
            print('\n',self.post_order_iter(),'\n')
        else:
            print('\nThe traversal you picked : ' + str(pick) + ' does not supported')
    
    # Pre-Order traversal
    # -- > ROOT --> LEFT --> RIGHT
    def print_pre_order(self, start, traversal):        
        if start:
            traversal += str(start.value) + '-'
            traversal = self.print_pre_order(start.left, traversal)
            traversal = self.print_pre_order(start.right, traversal)
        return traversal
    
    # In-Order traversal
    # --> LEFT --> ROOT --> RIGHT
    def print_in_order(self, start, traversal):
        if start:
            traversal = self.print_in_order(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.print_in_order(start.right, traversal)
        return traversal
    
    # Post-Order traversal
    # --> LEFT -- > RIGHT --> ROOT
    def print_post_order(self, start, traversal):
        if start:
            traversal = self.print_post_order(start.left, traversal)
            traversal = self.print_post_order(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal
    
    # Pre-Order traversal using Iterative Approach
    # ROOT --> LEFT --> RIGHT
    def pre_order_iter(self):
        if self.root is None:
            print('Tree is empty')
        else:
            traversal = ''
            cur_node = self.root
            s = []
            s.append(cur_node)
            while len(s) != 0:
                cur_node = s.pop()
                traversal += str(cur_node.value) + '-'
                if cur_node.right is not None:
                    s.append(cur_node.right)
                    
                if cur_node.left is not None:
                    s.append(cur_node.left)
                    
        return traversal

    # In-Order traversal using Iterative Approach 
    # LEFT --> ROOT --> RIGHT
    def in_order_iter(self):
        if self.root is None:
            print('The tree is empty..')
        elif self.root is not None:
            cur_node  = self.root
            s = []
            traversal = ''
            while True:
                if cur_node is not None:
                    s.append(cur_node)
                    cur_node = cur_node.left
                else:
                    if len(s) == 0:
                        break
                    cur_node = s.pop()
                    traversal += str(cur_node.value) + '-'
                    cur_node = cur_node.right
        return traversal
    
    # Post-Order traversal using Iterative Approach
    # LEFT --> RIGHT --> ROOT
    def post_order_iter(self):
        if self.root is None:
            print('Tree is empty..')
        else:
            s1 = []
            s2 = []
            s1.append(self.root)
            while len(s1) !=0:
                cur_node = s1.pop()
                s2.append(cur_node)
                if cur_node.left is not None:
                    s1.append(cur_node.left)
                if cur_node.right is not None:
                    s1.append(cur_node.right)
              
            traversal = ''
            while len(s2) !=0:
                node = s2.pop()
                traversal += str(node.value) + '-'
        return traversal

    # search an element in binary tree using recursive approach:
    def search_tree(self, val):
        if self.root is not None:
            return self._search_tree(self.root, val)
    
    def _search_tree(self, cur_node, val):
        if cur_node.value == val: return True

        if cur_node.value > val:
            if cur_node.left is not None:
                if cur_node.left.value == val:
                    return True
                else:
                    return self._search_tree(cur_node.left, val)
        elif cur_node.value < val:
            if cur_node.right is not None:
                if cur_node.right.value == val:
                    return True
                else:
                    return self._search_tree(cur_node.right, val)
        return False
    # search an element in binary tree using iterative approach
    def search_iterative(self,val):
        if self.root is not None:
            if self.root.value == val:
                return True
            else:
                cur_node = self.root
                while cur_node is not None:
                    if cur_node.value == val:
                        return True
                    # iterate through right node
                    elif cur_node.value < val:
                        cur_node = cur_node.right
                    # iterate through left node
                    elif cur_node.value > val:
                        cur_node = cur_node.left
        return False


# traverse through tree
tree = BinaryTree()
tree.make_tree()
#print(tree.search_iterative(20))
#print(tree.search_iterative(200))
print('------------------------')
print(tree.pre_order_iter())
tree.insert_iterative(Node(45))
print(tree.pre_order_iter())


