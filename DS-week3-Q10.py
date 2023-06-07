class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        if i==0:
            return
        
        parent = (i-1) // 2

        if self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_up(parent)

    def max_value(self):
        if self.heap is None:
            return None
        else:
            print("max_value = ", self.heap[0])

    def extract_max(self):
        if self.heap is None:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return max_value


    def heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

    def delete(self, x):
        if x not in self.heap:
            print("element not found")
            return
        index = self.heap.index(x)
        parent = (index-1) // 2
        self.heap.pop(index)
        self.heapify_up(parent)
        self.heapify(0)

    def sorted_heap(self):
        sorted_array = []
        while len(self.heap) > 0:
            max_val = self.extract_max()
            sorted_array.insert(0, max_val)
        return sorted_array
    
    def build_heap(self, array):
        self.heap = array
        n = len(array)
        last_parent = (n // 2) - 1

        for i in range(last_parent, -1, -1):
            self.heapify(i)
        return self.heap



heap = BinaryHeap()
heap.insert(3)
heap.insert(5)
heap.insert(7)
heap.insert(10)
heap.insert(8)

print(heap.heap)
x = heap.sorted_heap()
print(x)

array = [4,3,11,2,9,0]
result = heap.build_heap(array)
print(result)