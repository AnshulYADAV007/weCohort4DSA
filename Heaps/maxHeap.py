class MaxHeap:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def size(self):
        return len(self.heap)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            maxEle = self.heap[0]
            self.__swap(0, -1)
            self.heap.pop()
            self.__maxHeapify(0)
            return maxEle
        elif len(self.heap) == 1:
            maxEle = self.heap[0]
            self.heap.pop()
            return maxEle
        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.__swap(parent, index)
            self.__percolateUp(parent)

    def __swap(self, parent, index):
        self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

    def __maxHeapify(self, index):
        largest = self.__getLargest(index, index * 2 + 1, index * 2 + 2)
        if largest != index:
            self.__swap(largest, index)
            self.__maxHeapify(largest)

    def __getLargest(self, index, left, right):
        answer = index
        if left < len(self.heap) and self.heap[answer] < self.heap[left]:
            answer = left
        if right < len(self.heap) and self.heap[answer] < self.heap[right]:
            answer = right
        return answer


# heap = MaxHeap()
# heap.insert(9)
# heap.insert(8)
# heap.insert(7)
# heap.insert(10)
# print("After inserting 9, 8, 7, 10", heap.heap)
# heap.removeMax()
# print("After removing max", heap.heap)
