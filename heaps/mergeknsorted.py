"""Merge K sorted arrays, size N each."""
class Node(object):
    def __init__(self, arr):
        self.arr = arr
        self.iter = iter(self.arr)
        self.cur = None
        
        self.getnext()
        
    def getnext(self):
        try:
            n = next(self.iter)
            self.cur = n
        except:
            self.cur = None
            
        return self.getcur()
        
    def getcur(self):
        return self.cur

class CustomMinHeap(object):
    def __init__(self):
        """Heap starts from index 1."""
        self.heap = [None]
        self.heapsize = 0

    def getparent(self, index):
        return (index // 2)

    def getright(self, index):
        return (2 * index) + 1

    def getleft(self, index):
        return (2 * index)

    def swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]
        
    def getmin(self):
        if self.heapsize > 0:
            return self.heap[1]
        else:
            return None

    ## PUSH AND HEAPIFY UP ##
    
    def push(self, node):
        """Push a node into the heap."""
        self.heap.append(node)
        self.heapsize += 1
        
        self.heapify_up(self.heapsize)

    def heapify_up(self, index):
        parent = self.getparent(index)
        
        if parent > 0 and self.heap[parent].getcur() > self.heap[index].getcur():
            # Swap parent with index
            self.swap(parent, index)
            # moving to check if the parent satisfies the minheap property
            self.heapify_up(parent)

    ## POP AND HEAPIFY DOWN ##

    def pop(self):
        """Pop and return the minmum element from the heap.
        
        Custom: move the root to the next element and fix heap invariant
        if no next element, pop that from the heap
        """
        if not self.heapsize > 0:
            return None
            
        root = 1
        element = self.heap[root].getcur()
        
        if self.heap[root].getnext():
            # move on to heapifying down
            pass
        else:
            # Swap Root (popped element) with the last element in heap
            self.swap(root, self.heapsize)

            # Removing the last element after swapping
            self.heapsize -= 1
            self.heap.pop()

        # Heapify Down
        self.heapify_down(root)
        
        return element

    def heapify_down(self, index):
        smallest = index
        
        left = self.getleft(index)
        right = self.getright(index)
        
        if left <= self.heapsize and self.heap[left].getcur() < self.heap[smallest].getcur():
            smallest = left

        if right <= self.heapsize and self.heap[right].getcur() < self.heap[smallest].getcur():
            smallest = right

        if smallest != index:
            # Swap parent with index
            self.swap(smallest, index)
        
            # moving to check if the "smallest" node's index satisfies the minheap property
            self.heapify_down(smallest)
        
def mergearrays(arrs):
    minheap = CustomMinHeap()
    result = []
    
    for arr in arrs:
        node = Node(arr)
        minheap.push(node)
        
    while minheap.getmin():
        result.append(minheap.pop())
        
    return result

def test_mergearrays_one():
    arrs = [
        [9, 11, 18, 24, 31, 35],
        [0, 0, 3, 11, 16, 19],
        [0, 8, 10, 15, 21, 22],
        [0, 3, 8, 8, 11, 14],
        [0, 6, 11, 11, 12, 18],
        [5, 10, 14, 18, 26, 30],
        [6, 9, 11, 13, 22, 25],
        [3, 7, 13, 18, 22, 25],
        [3, 12, 16, 25, 27, 36]
    ]
    res = mergearrays(arrs)
    exp =  [0,  0,  0,  0,  0,  3,  3,  3,  3,  5,  6,  6,  7,  8,  8,  8,  9, 
            9,  10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 13, 13, 14, 14, 15, 16,
            16, 18, 18, 18, 18, 19, 21, 22, 22, 22, 24, 25, 25, 25, 26, 27, 30, 31, 35, 36]

    assert(res==exp)
