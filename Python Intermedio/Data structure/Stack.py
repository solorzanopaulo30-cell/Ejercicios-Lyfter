

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack():
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("El stack esta vacio")
            return None
        popped_node = self.top
        self.top = self.top.next_node
        return popped_node.value

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next_node


stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

stack.print_stack()

print("Saco:", stack.pop())
stack.print_stack()