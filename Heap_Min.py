
class Heap_Min:

    def __init__(self, items = []):
        self.list = []
        
        for i in items:
            self.push(i)    

    # push an item into the list
    def push(self, item):

        if self.list == [] :
            self.list.append(item)
        elif self.size(self.list) == 1:
            if self.list[0] > item:
                self.list.append(item)
                self.list[0], self.list[1] = self.list[1], self.list[0]
        else:
            self.list.append(item)
            self.build_min_heap(self.list)
    
    # Returns Min heap peek item of the tree
    def peek(self):
        if self.list == []:
            return
        return self.list[0]

    # remove min heap item of the tree
    def pop(self):
        # swap the peek item with the last item of the list 
        self.list[0], self.list[self.size(self.list)] = self.list[self.size(self.list)], self.list[0]
        poped = self.list.pop()
        #print('After pop ',self.list)
        self.build_min_heap(self.list)
        
        return poped
    
    # building min heap tree
    def build_min_heap(self, arr):
        n = self.size(arr)
        for i in range(n//2, -1, -1):
            self.min_heapify(arr, i, n)
    
    # generate min heapify tree
    def min_heapify(self,arr, i, n):
        left  = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left <= n and arr[left] < arr[i]:
            smallest = left
        
        if right <= n and arr[right] < arr[smallest]:
            smallest = right
        
        if smallest != i:
            arr[i] , arr[smallest] = arr[smallest], arr[i]
            self.min_heapify(arr, smallest, n)
                    
    # returns the tree list
    def print_tree(self):
        return self.list
    
    # heap sort method ascending order
    def heapsort(self):
        self.build_min_heap(self.list)
        n = self.size(self.list)
        arr = self.list
        b = []
        HeapSize = self.size(arr)
        for i in range(n, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            b.append(arr[i])
            arr = arr[:-1]
            HeapSize = HeapSize - 1
            self.min_heapify(arr, 0, i-1)

        return b
    # hepa sort method descending oreder
    def heapsort2(self):
        self.build_min_heap(self.list)
        n = self.size(self.list)
        arr = self.list
        for i in range(n, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.min_heapify(arr, 0, i-1)

        return arr

    # returns the size of the list
    def size(self,arr):
        return len(arr) - 1


if __name__ == '__main__':
    lst = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    H = Heap_Min(lst)
    #for i in lst:
    #    H.push(i)
    print('Min Heap tree is : ', H.print_tree())
    H.push(5)
    print('Min Heap tree is : ', H.print_tree())
    print('Peek item : ',H.peek())
    print('Poped item : ', H.pop())
    print('Heap sort desc : ', H.heapsort2())

    
    