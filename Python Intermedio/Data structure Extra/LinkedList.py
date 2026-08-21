

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node is not None:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def print_all(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += " -> "
            current = current.next_node
        print(result)


ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()
ll.insert_back(30)
ll.print_all()
ll.delete(10)
ll.print_all()