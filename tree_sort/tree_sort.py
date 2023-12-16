from visualize import visualize_sorting


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    elif key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def in_order_traversal(root):
    result = []
    if root:
        result = in_order_traversal(root.left)
        result.append(root.value)
        result = result + in_order_traversal(root.right)
    return result


def tree_sort(arr):
    root = None
    for item in arr:
        root = insert(root, item)

    visualize_sorting(root)

    return in_order_traversal(root)
