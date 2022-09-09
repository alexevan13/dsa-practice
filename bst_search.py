class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def generate_bst(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    return TreeNode(val=arr[mid], left=generate_bst(arr[:mid]), right=generate_bst(arr[mid + 1:]))


answer = []


def create_bst():
    arr = [i for i in range(10)]
    bst = generate_bst(arr)
    return bst


def preorder_traverse_recursive(root):
    # nlr
    if not root:
        return
    answer.append(root.val)
    preorder_traverse_recursive(root.left)
    preorder_traverse_recursive(root.right)


def inorder_traverse_recursive(root):
    # lnr
    if not root:
        return
    inorder_traverse_recursive(root.left)
    answer.append(root.val)
    inorder_traverse_recursive(root.right)


def postorder_traverse_recursive(root):
    # lrn
    if not root:
        return
    postorder_traverse_recursive(root.left)
    postorder_traverse_recursive(root.right)
    answer.append(root.val)


def preorder_traverse_iterative(root):
    stack = [root]
    while len(stack) > 0:
        elem = stack.pop()
        if elem:
            answer.append(elem.val)
            stack.append(elem.right)
            stack.append(elem.left)


def inorder_traverse_iterative(root):
    stack = [root]
    while len(stack) > 0:
        elem = stack.pop()
        if elem:
            stack.append(elem.right)
            answer.append(elem.val)
            stack.append(elem.left)


def postorder_traverse_iterative(root):
    stack = [root]
    while len(stack) > 0:
        elem = stack.pop()
        if elem:
            stack.append(elem.right)
            stack.append(elem.left)
            answer.append(elem.val)


bst = create_bst()
print("******* TREE *******")
bst.display()
print("******* PREORDER RECURSIVE *******")
answer.clear()
preorder_traverse_recursive(bst)
print(answer)
print("******* INORDER RECURSIVE *******")
answer.clear()
inorder_traverse_recursive(bst)
print(answer)
print("******* POSTORDER RECURSIVE *******")
answer.clear()
postorder_traverse_recursive(bst)
print(answer)
print("******* PREORDER ITERATIVE *******")
answer.clear()
preorder_traverse_iterative(bst)
print(answer)
print("******* INORDER ITERATIVE *******")
answer.clear()
inorder_traverse_recursive(bst)
print(answer)
print("******* POSTORDER ITERATIVE *******")
answer.clear()
postorder_traverse_iterative(bst)
print(answer)