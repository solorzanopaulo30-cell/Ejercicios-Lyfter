class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self):
        self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node is None:
            return
        self._print_in_order(node.left)
        print(node.value)
        self._print_in_order(node.right)


class SortState():
    def __init__(self):
        self.prev_node = None
        self.swapped = False


def bubble_sort_tree(tree):
    def one_pass(node, state):
        if node is None:
            return
        one_pass(node.left, state)
        if state.prev_node is not None and state.prev_node.value > node.value:
            print(f"Intercambiando {state.prev_node.value} y {node.value}")
            state.prev_node.value, node.value = node.value, state.prev_node.value
            state.swapped = True
        state.prev_node = node
        one_pass(node.right, state)

    keep_going = True
    while keep_going:
        state = SortState()
        one_pass(tree.root, state)
        keep_going = state.swapped


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

bubble_sort_tree(tree)
tree.print_tree()