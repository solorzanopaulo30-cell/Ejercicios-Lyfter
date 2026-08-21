

class Node():
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev_node is not None:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node

                if current.next_node is not None:
                    current.next_node.prev_node = current.prev_node
                else:
                    self.tail = current.prev_node
                return
            current = current.next_node

    def print_forward(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += " -> "
            current = current.next_node
        print(result)

    def print_backward(self):
        current = self.tail
        result = ""
        while current is not None:
            result += str(current.data)
            if current.prev_node is not None:
                result += " -> "
            current = current.prev_node
        print(result)


dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.print_forward()
dll.print_backward()

dll.prepend("X")
dll.print_forward()
dll.print_backward()

dll.delete("B")
dll.print_forward()
dll.print_backward()