class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert at the end."""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, value):
        """Delete first occurrence of value."""
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def traverse(self):
        """Return list of all values."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def __str__(self):
        return "->".join(str(v) for v in self.traverse())


# Rooted Tree using linked lists for children
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of TreeNode

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        """Preorder traversal, returns list of values."""
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse())
        return result

    def __str__(self):
        return f"{self.value}({', '.join(str(child) for child in self.children)})" if self.children else str(self.value)


# Example for SinglyLinkedList and TreeNode
if __name__ == "__main__":
    print("Singly Linked List Example:")
    ll = SinglyLinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(20)
    print("List:", ll)
    ll.delete(10)
    print("After deleting 10:", ll)
    print("Traverse:", ll.traverse())

    print("\nRooted Tree Example:")
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode(4))
    child1.add_child(TreeNode(5))
    print("Tree (preorder traversal):", root.traverse())
    print("Tree structure:", root)