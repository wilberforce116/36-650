class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.previous = None


# Class to create a Linked List
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail
        self.size = 1 if tail else 0

    # Insert a node in a linked list
    def insert(self, data):
        self.size += 1
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            node.previous = self.tail
            self.tail = node

    # Delete a node in a linked list
    # Note: This function only deletes the first instance of the value
    def delete(self, value):
        if not self.tail:
            return "List is already empty"

        current = self.tail
        
        if self.tail.data == value:
            self.tail = current.previous
            return

        while(current.previous):
            if current.previous.data == value:
                current.previous = current.previous.previous
                return
        
        print("Node not found")

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    def search(self, value):
        current = self.tail
        while(current):
            if current.data == value:
                return True
            current = current.previous
        return False


linked_list = ReverseLinkedList(Node(11))
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The linked list is (after insertion):")
linked_list.print_list()

linked_list.delete(6)
print("After deletion, the linked list now reads:")
linked_list.print_list()

print("Does 5 exist in this linked list?")
linked_list.search(5)

print("Does 17 exist in this linked list?")
linked_list.search(17)
