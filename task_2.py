from task_1 import BSTree, tree

# Завдання 2. Додайте до класу Tree методи пошуку мінімального і максимального
# значення елементів в бінарному дереві пошуку.


print('--- Task 2 ---')


# Знаходить мінімальне значення.
def get_min(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.val


# Знаходить максимальне значення.
def get_max(self):
    current = self
    while current.right is not None:
        current = current.right
    return current.val


print('Min:', tree.get_min())
print('Max:', tree.get_max())