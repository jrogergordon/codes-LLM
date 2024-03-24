class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def level_order(root, desired):
    if root is None:
        return 0

    queue = []
    level = 0

    queue.append(root)

    while queue:
        size = len(queue)
        level += 1

        while size > 0:
            temp = queue[0]
            queue.pop(0)

            if temp.data == desired:
                return level

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

            size -= 1

    return -1


# Test the function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(level_order(root, 1))  # Output: 3 
print(level_order(root, 6))  # Output: -1