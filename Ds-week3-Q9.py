class Max_heap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        if i == 0:
            return
        
        parent = (i-1) // 2

        if self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_up(parent)

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
        right = 2*1 + 2
        largest = i

        if left<len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        if right<len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest!=i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

    def delete(self, data):
        if data not in self.heap:
            print("element not found")
            return
        index = self.heap.index(data)
        parent = (index-1) // 2
        self.heap.pop(index)
        self.heapify_up(parent)
        self.heapify(0)
        print("done")

    def heap_sort(self):
        sorted_array = []
        while len(self.heap) > 0:
            max_val = self.extract_max()
            sorted_array.insert(0, max_val)
        return sorted_array

heap = Max_heap()
heap.insert(2)
heap.insert(6)
heap.insert(3)
heap.insert(12)
heap.insert(9)

print(heap.heap)

x= heap.heap_sort()
print("Sorted array:", x)