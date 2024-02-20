class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, current.prev)
            current = current.next

    def find_and_delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                # Found the node, delete it
                if current == self.head:
                    # If the node is the head, update the head
                    self.head = current.next
                else:
                    # Otherwise, update the prev node's next pointer
                    current.prev.next = current.next
                # Update the tail if necessary
                if current == self.tail:
                    self.tail = current.prev
                # Delete the node
                current = None
                return True
            current = current.next
        return False
    
# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.find_and_delete(3)
ll.traverse()