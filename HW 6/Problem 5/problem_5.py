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
    
    def remove_dups(self):
        first = self.head
        while(first):
            second = first.next
            just_before_second = first
            while(second):
                if first.data == second.data:
                    just_before_second.next = just_before_second.next.next
                else:
                    just_before_second = second
                second = second.next
            first = first.next


first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

print("The linked list is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the linked list is now:")
linked_list.print_list()
