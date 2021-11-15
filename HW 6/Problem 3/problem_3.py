class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 1 if head else 0

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Insert a node in a linked list
    def insert(self, data):
        self.size += 1
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
    
    def sort(self):

        for i in range(self.size):

            current = self.head
            current_plus = self.head.next
            current_minus = None

            for j in range(self.size - i - 1):
                if current.data > current_plus.data:
                    current.next = current_plus.next
                    current_plus.next = current
                    if not current_minus:
                        self.head = current_plus
                    else:
                        current_minus.next = current_plus
                    current_minus = current_plus
                    current_plus = current.next
                else:
                    current_minus = current
                    current = current.next
                    current_plus = current.next



first_node = Node(7)
linked_list = LinkedList(first_node)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(8)
linked_list.insert(7)

print("The linked list is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the linked list is now:")
linked_list.print_list()
