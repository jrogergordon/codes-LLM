class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def flatten_tree(root):
    if not root:
        return None

    # Create a stack to hold the nodes to visit
    stack = [root]

    # Create a pointer to the current node
    current = root

    # Iterate until the stack is empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # If the node has a left child, add it to the stack
        if node.left:
            stack.append(node.left)

        # If the node has a right child, add it to the stack
        if node.right:
            stack.append(node.right)

        # Connect the current node to the next node in the stack
        current.right = node
        node.left = None
        current = node

    # Return the flattened tree
    return current

# Create a sample binary tree
s = TreeNode(1)
s.left = TreeNode(2)
s.right = TreeNode(3)
s.left.left = TreeNode(4)
s.left.right = TreeNode(5)
s.right.right = TreeNode(6)

# Flatten the tree
ans = flatten_tree(s)

# Print the flattened tree (right child of each node should point to the next node in preorder traversal)
current = ans
while current:
    print(current.val, end=" -> ")
    current = current.right