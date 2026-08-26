class Node():
    def __init__(self, value):
        self.value = value
        self.prev_node = None
        self.next_node = None


class Deque():
    def __init__(self):
        self.left = None
        self.right = None

    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev_node = self.right
            self.right.next_node = new_node
            self.right = new_node

    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next_node = self.left
            self.left.prev_node = new_node
            self.left = new_node

    def pop_right(self):
        if self.right is None:
            print("El deque esta vacio")
            return None
        popped_node = self.right
        self.right = popped_node.prev_node
        if self.right is None:
            self.left = None
        else:
            self.right.next_node = None
        return popped_node.value

    def pop_left(self):
        if self.left is None:
            print("El deque esta vacio")
            return None
        popped_node = self.left
        self.left = popped_node.next_node
        if self.left is None:
            self.right = None
        else:
            self.left.prev_node = None
        return popped_node.value

    def print_deque(self):
        current = self.left
        while current is not None:
            print(current.value)
            current = current.next_node


def bubble_sort_deque(deque):
    if deque.left is None:
        return
    swapped = True
    while swapped:
        swapped = False
        current = deque.left
        while current.next_node is not None:
            print(f"Comparando {current.value} con {current.next_node.value}")
            if current.value > current.next_node.value:
                print("Valores intercambiados")
                current.value, current.next_node.value = current.next_node.value, current.value
                swapped = True
            current = current.next_node


deque = Deque()
deque.push_right(5)
deque.push_right(1)
deque.push_right(9)
deque.push_right(3)

bubble_sort_deque(deque)
deque.print_deque()