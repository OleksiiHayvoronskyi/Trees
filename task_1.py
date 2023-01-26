# Завдання 1. Додайте до класу Tree метод, який реалізує додавання до бінарного
# дерева пошуку нових елементів зі списку. Метод має містити функціонал, який
# перевіряє дані зі списку на відповідність до правил формування бінарного
# дерева пошуку.


print('\n--- Task 1 ---')


# Клас Binary Search Tree
class BSTree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

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
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTree(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        if self.right == None:
            return False
        return self.right.exists(val)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()



tree = BSTree(1)
#print('tree:', tree.val)
tree.left = BSTree(2)
#print('left:', tree.left.val)
tree.left.left = BSTree(3)
#print('left_left:', tree.left.left.val)
tree.left.right = BSTree(4)
#print('left_right:', tree.left.left.val)
tree.right = BSTree(5)
#print('right:', tree.right.val)

#tree.insert(45)

# tree.insert(12)
# tree.insert(8)
# tree.insert(22)
# tree.insert(14)
# tree.insert(4)
# tree.insert(3)

print(tree.print_tree())



# nodes = [7, 3, 2, 6, 9, None, 1, 5, 8, 4, 24]
#
# print('Given list of nodes:', nodes)
# # Додавання елементів зі списку до дерева.
# binary_tree = build(nodes)
# print('Binary tree with values from the list:', binary_tree)
#
# # Перевіряє відповідність до правил.
# print('Properties of the tree: \n', binary_tree.properties)
