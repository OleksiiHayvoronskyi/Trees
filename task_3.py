from task_1 import BSTree, tree

# Завдання 3. Додайте до класу Tree метод видалення елементів в бінарному
# дереві пошуку.


print('--- Task 3 ---')


def delete(self, val):
    if self == None:
        return self
    if val < self.val:
        if self.left:
            self.left = self.left.delete(val)
        return self
    if val > self.val:
        if self.right:
            self.right = self.right.delete(val)
        return self
    if self.right == None:
        return self.left
    if self.left == None:
        return self.right
    min_larger_node = self.right
    while min_larger_node.left:
        min_larger_node = min_larger_node.left
    self.val = min_larger_node.val
    self.right = self.right.delete(min_larger_node.val)
    return self


print('Deleted', tree.delete())
