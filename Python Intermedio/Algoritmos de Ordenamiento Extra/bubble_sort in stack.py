

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


def bubble_sort_stack(stack):
    if stack.top is None:
        return
    swapped = True
    while swapped:
        swapped = False
        current = stack.top
        while current.next_node is not None:
            print(f"Comparando {current.value} con {current.next_node.value}")
            if current.value > current.next_node.value:
                print("Valores intercambiados")
                current.value, current.next_node.value = current.next_node.value, current.value
                swapped = True
            current = current.next_node


stack = Stack()
stack.push(5)
stack.push(1)
stack.push(9)
stack.push(3)

bubble_sort_stack(stack)
stack.print_stack()