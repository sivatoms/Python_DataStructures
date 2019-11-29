
class Heap_Max:
    # initializig the heap tree
    def __init__(self, items = None):
        self.list = []
        for i in items:
            self.push(i)
    
    # inserting items or nodes onto heap
    def push(self, item):
        if self.list == []:
            self.list.append(item)
        elif self.size(self.list) == 1:
            if self.list[0] < item:
                self.list.append(item)
                self.list[0], self.list[1] = self.list[1], self.list[0]
            else:
                self.list.append(item)
        else:
            self.list.append(item)
            self.build_max_heap()
    
    # peek of the max heap tree
    def peek(self):
        if self.list == []:
            return
        return self.list[0]
    
    # pop the max heap item from the tree
    def pop(self):
        # swap the last item of the list with the peek item of the list
        self.list[0], self.list[self.size(self.list)] = self.list[self.size(self.list)], self.list[0]
        # pop the peek item
        poped = self.list.pop()
        # build the max heap for the last swaped item of the list
        self.build_max_heap()

        return poped

            
    # Max heap function to create a Heap tree
    def max_hepify(self,arr, i, n):
        
        left  = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left <= n and arr[left] > arr[i]:
            largest = left
        
        if right <= n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]

            self.max_hepify(arr, largest, n)

    # Building Max Heap tree
    def build_max_heap(self):
        n = self.size(self.list)
        arr = self.list

        for i in range(n//2, -1, -1):
            self.max_hepify(arr, i, n)

    # returns the size of the Heap List
    def size(self, arr):
        return len(arr)-1

    # Returns the entire list after creating heap
    def print_max_heap(self):
        return self.list

    #  Heap Sort Algorithm
    def heapsort(self):
        n = self.size(self.list)
        arr = self.list
        for i in range(n, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.max_hepify(arr, 0 , i-1)
        return arr


if __name__ == '__main__':
    
    lst = [8, 7, 1, 0, 2, 3, 5, 6, 4]
    H = Heap_Max(lst)
    #for i in lst:
    #    H.insert_node(i)
    #H.build_max_heap()
    print('After Max Heap : ',H.print_max_heap())
    #print('After Sort : ', H.heapsort())
    print('Poped item is : ', H.pop())
    print('Peek item is : ', H.peek())
