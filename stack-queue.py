class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top >= self.capacity - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return str(self.data[:self.top+1])


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise Exception("Queue Overflow")
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue Underflow")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peek(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.size == 0:
            return "[]"
        items = []
        idx = self.front
        for _ in range(self.size):
            items.append(self.data[idx])
            idx = (idx + 1) % self.capacity
        return str(items)

# stack and queue examples
if __name__ == "__main__":
    print("Stack :")
    stack = Stack(5)
    stack.push(5)
    stack.push(10)
    stack.push(20)
    print("Stack:", stack)
    # Pop an element using LIFO order
    print("Pop:", stack.pop())
    print("After pop:", stack)
    print("Peek:", stack.peek())

    print("\nQueue :")
    queue = Queue(5)
    queue.enqueue(5)
    queue.enqueue(20)
    queue.enqueue(10)
    print("Queue:", queue)
    # Dequeue an element using FIFO order
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue)
    print("Peek:", queue.peek())