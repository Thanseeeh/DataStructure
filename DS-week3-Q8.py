class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertion(self, k):
        self.heap.append(k)
        self.bubbleup(len(self.heap) - 1)

    def bubbleup(self, i):
        if i == 0:
            return  # Base case: current node is the root

        parent = (i - 1) // 2

        if self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubbleup(parent)

    def extractmax(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop(0)
        self.heapify(0)
        return max_val

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        large = i

        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            large = l
        if r < len(self.heap) and self.heap[r] > self.heap[large]:
            large = r
        if large != i:
            self.heap[i], self.heap[large] = self.heap[large], self.heap[i]
            self.heapify(large)

    def delete(self, y):
        if y not in self.heap:
            print("not found")
            return
        index = self.heap.index(y)
        self.heap.pop(index)
        parent = (index - 1) // 2  # Calculate the parent index
        self.bubbleup(parent)  # Pass the parent index to bubbleup
        self.heapify(0)  # Start heapify from the root
        print("done")


x = MaxHeap()
x.insertion(70)
x.insertion(60)
x.insertion(50)
x.insertion(40)
x.insertion(30)
x.insertion(20)
x.insertion(10)
x.delete(30)
print(x.heap)
