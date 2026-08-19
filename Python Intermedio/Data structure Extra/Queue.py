

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("the queue is empthy")
            return None
        removed_node = self.front
        self.front = removed_node.next_node
        if self.front is None:
            self.rear = None
        return removed_node.data

    def print_all(self):
        current = self.front
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += " -> "
            current = current.next_node
        print(result)


q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()
print(q.dequeue())
q.print_all()