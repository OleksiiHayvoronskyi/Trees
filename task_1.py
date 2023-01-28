# Завдання 1. Додайте до класу Tree метод, який реалізує додавання до бінарного
# дерева пошуку нових елементів. Метод має містити функціонал, який
# перевіряє дані зі списку на відповідність до правил формування бінарного
# дерева пошуку.

print('\n--- Task 1 ---')


# Клас Binary Search Tree
class BSTree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    # Функція вставки нового елемента.
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTree(val)
            print('Added to the left:', val, '\n')
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTree(val)
        print('Added to the right:', val)

    # Функція пошуку мінімального елемента.
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    # Функція пошуку максимального елемента.
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    # Функція перевірки, чи існує елемент.
    def exists(self, val):
        if val == self.val:
            print('\nFound:', val)
            return True

        elif val < self.val:
            if self.left is None:
                print('Not found:', val, '\n')
                return False
            return self.left.exists(val)

        elif self.right is None:
            print('Does not exist:', val, '\n')
            return False
        return self.right.exists(val)

        # Функція видалення елемента.
    def delete(self, val):
        if self is None:
            return self

        elif val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        print(val, 'was deleted')

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

        return  self

        # Функція друку.
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


tree = BSTree(12)
# print('tree:', tree.val)
tree.left = BSTree(2)
# print('left:', tree.left.val)
tree.left = BSTree(3)
# print('left_left:', tree.left.left.val)
tree.left = BSTree(4)
# print('left_right:', tree.left.right.val)
tree.right = BSTree(5)
# print('right:', tree.right.val)
tree.right.left = BSTree(23)


tree.insert(25)
tree.insert(7)

tree.exists(7)
tree.exists(3)

print("Binary tree:")
tree.print_tree()
