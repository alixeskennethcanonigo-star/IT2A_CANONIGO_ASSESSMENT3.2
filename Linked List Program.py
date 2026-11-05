# Assessment 3.2: Linked List Implementation
# Name: CANONIGO, ALEXIS KENNETH (BSIT 2A)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def display(self):
        if not self.head:
            print("Empty")
            return
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" → ".join(elements))


def main():
    # Step 1: Create an empty linked list
    ll = LinkedList()

    # Step 2: Add a node for each letter in CANONIGO, in order
    letters = ['C', 'A', 'N', 'O', 'N', 'I', 'G', 'O']
    for letter in letters:
        ll.append(letter)

    # Step 3: Display the linked list
    ll.display()

    # Step 4: While the linked list is not empty, delete the last node and display the remaining list
    while ll.head is not None:
        ll.delete_last()
        ll.display()


if __name__ == "__main__":
    main()