class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class double:
    def __init__(self):
        self.start = None


    def insertionfirst(self,value):
        newnode = node(value)
        if self.start==None:
            self.start = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode


    def view(self):
        if self.start==None:
            print('list is empty')
        else:
            temp = self.start
            while temp.next!=None:
                print(temp.data)
                temp = temp.next
            print(self.tail.data)



    def count(self):
        self.sum = 1
        temp = self.start
        while temp.next!=None:
            temp = temp.next
            self.sum+=1


    def insertionlast(self,value):
        value = node(value)
        if self.start==None:
            self.start = value
            self.tail = value
        else:
            self.tail.next = value
            value.prev = self.tail
            self.tail = value

      
    def insertionspec(self,pos,value):
        self.count()
        if self.start == None:
            print('list is empty')
        elif pos > self.sum:
            print('value not found')
        elif pos == 0:
            newnode = node(value)
            newnode.next =self.start 
            self.start = newnode
            self.start.next.prev = self.start
        elif pos == 1:
            newnode = node(value)
            temp = self.start
            newnode.next=temp.next
            newnode.prev = temp
            temp.next = newnode
            newnode.next.prev = newnode
            temp = newnode
        elif pos == self.sum:
            self.insertionlast(value)
        else:
            value = node(value) 
            temp = self.start
            i = 1
            while (i <= pos -1):
                temp = temp.next
                i+=1
            value.prev = temp
            value.next = temp.next
            temp.next = value
            value.next.prev = value
            temp = value




llist = double()
llist.insertionfirst('lol')
llist.insertionfirst(82)
llist.insertionfirst(999)
llist.insertionfirst(499)
llist.insertionfirst(800)
llist.insertionfirst(2200)
llist.view()

