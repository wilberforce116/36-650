class Queue:
    def __init__(self):
        self.inner_list = []
        self.top = 0

    def enqueue(self, value):
        self.inner_list.insert(self.top, value)
        self.top += 1
                
    def dequeue(self):
        value = self.inner_list.pop(0)
        self.top -= 1
        return(value)
    
    def delete(self, value):
        for i in range(len(self.inner_list)):
            temp = self.dequeue()
            if temp != value:
                self.enqueue(temp)


        
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

print("Before deletion, the queue contains:")
print(obj.inner_list)

obj.delete(7)
print("After deletion, the queue now reads:")
print(obj.inner_list) 
