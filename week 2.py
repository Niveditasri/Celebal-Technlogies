# Node class to represent each node in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # List is empty
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the list
    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete the nth node (1-based index)
    def delete_nth_node(self, n):
        if not self.head:
            print("Error: Cannot delete from an empty list.")
            return

        if n <= 0:
            print("Error: Invalid index. Index must be >= 1.")
            return

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count = 1

        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            print("Error: Index out of range.")
            return

        print(f"Deleting node at position {n} with value {current.next.data}")
        current.next = current.next.next

# Testing the implementation
if __name__ == "__main__":
    ll = LinkedList()

    # Add elements to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    print("Initial list:")
    ll.print_list()

    # Delete node at position 3
    ll.delete_nth_node(3)
    print("List after deleting 3rd node:")
    ll.print_list()

    # Try deleting at invalid position
    ll.delete_nth_node(10)

    # Try deleting from an empty list
    empty_ll = LinkedList()
    empty_ll.delete_nth_node(1)
