class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack Implementation using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None

# Queue Implementation using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def is_empty(self):
        return self.front is None

# Example usage
if __name__ == "__main__":
    # Stack example
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack top:", stack.peek())  # Output: 30
    print("Popped from stack:", stack.pop())  # Output: 30
    print("Stack top after pop:", stack.peek())  # Output: 20

    # Queue example
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue front:", queue.peek())  # Output: 1
    print("Dequeued from queue:", queue.dequeue())  # Output: 1
    print("Queue front after dequeue:", queue.peek())  # Output: 2

