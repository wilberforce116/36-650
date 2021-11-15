class Node(object):
    def __init__(self, data = None):
        self.small = None
        self.big = None
        self.too_big = None
        self.data = data

    def insert(self, data):
        if self.data:
            if (data - self.data) < 0:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif (data - self.data) >= 0 and (data - self.data) < 10:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            else:
                if self.too_big is None:
                    self.too_big = Node(data)
                else:
                    self.too_big.insert(data)
        else:
            self.data = data

    def replace_branch(self, value):
        lower_branch = self.traversal()
        lower_branch.remove(value)
        self.__init__()
        for i in lower_branch:
            self.insert(i)

    def delete(self, value):
        current = self

        if self.data == value:
            self.replace_branch(value)
            return
        
        if value < current.data:
            current = current.small
            current.delete(value)
            return

        if value > current.data and value < current.data + 10:
            current = current.big
            current.delete(value)
            return

        if value >= current.data + 10:
            current = current.too_big
            current.delete(value)
            return

    def traversal(self):
        flattened_tree = []
        if self.small:
            flattened_tree += self.small.traversal()
        if self.data:
            flattened_tree += [self.data]
        if self.big:
            flattened_tree += self.big.traversal()
        if self.too_big:
            flattened_tree += self.too_big.traversal()
        return(flattened_tree)

root = Node(20)
root.insert(40)
root.insert(29)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal() function:")
print(root.traversal())

root.delete(40)

print("After deletion, the tree now contains:")
print(root.traversal())
