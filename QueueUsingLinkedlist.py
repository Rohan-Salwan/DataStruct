class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.start = None
        self.tail = None
    
    def enque(self,item):
        newnode = node(item)
        if self.start ==None and self.tail == None:
            self.start = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def deque(self):
        if self.start ==None and self.tail == None:
            print('queue is underflow')
        else:
            self.start = self.start.next


    def view(self):
        if self.start == None and self.tail == None:
            print('que is empty')
        else:
            temp = self.start
            while temp!=None:
                print(temp.data)
                temp = temp.next


boy = queue()
boy.enque(14)
boy.enque(22)
boy.enque(99)
boy.enque('bhai')
boy.enque('lol')
boy.view()
print('')
boy.deque()
boy.view()
print('')
boy.deque()
boy.view()
